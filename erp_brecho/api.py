import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_available_items(category=None, size=None, limit=100):
    """
    API para buscar itens disponíveis no catálogo
    Uso: /api/method/erpnext.api.get_available_items?category=Vestidos&size=M
    """
    
    warehouse = 'Loja Brechó - GE'
    
    # Construir filtros
    conditions = []
    values = []
    
    conditions.append("i.disabled = 0")
    conditions.append("i.is_stock_item = 1")
    conditions.append("b.warehouse = %s")
    values.append(warehouse)
    conditions.append("b.actual_qty > 0")
    
    if category:
        conditions.append("i.item_group = %s")
        values.append(category)
    
    if size:
        conditions.append("i.custom_tamanho = %s")
        values.append(size)
    
    where_clause = " AND ".join(conditions)
    
    # Query
    query = f"""
        SELECT DISTINCT
            i.name,
            i.item_code,
            i.item_name,
            i.image,
            i.standard_rate,
            i.item_group,
            i.custom_tamanho as tamanho,
            i.custom_cor_principal as cor_principal,
            i.custom_estado_de_conservação as estado_conservacao,
            i.custom_marca_original as marca,
            i.description,
            b.actual_qty as quantidade
        FROM `tabItem` i
        INNER JOIN `tabBin` b ON b.item_code = i.name
        WHERE {where_clause}
        ORDER BY i.creation DESC
        LIMIT %s
    """
    
    values.append(int(limit))
    
    items = frappe.db.sql(query, tuple(values), as_dict=1)
    
    # Processar itens
    for item in items:
        # Formatar preço
        item['preco_formatado'] = 'R$ %.2f' % (item.standard_rate or 0)
        
        # Imagem padrão
        if not item.image:
            item.image = '/assets/frappe/images/placeholder-image.jpg'
        
        # URL amigável
        item['url'] = '/produto/' + item.item_code.lower()
        
        # Remover campos None
        for key in list(item.keys()):
            if item[key] is None:
                item[key] = ''
    
    return {
        'items': items,
        'total': len(items),
        'warehouse': warehouse
    }


@frappe.whitelist(allow_guest=True)
def get_item_details(item_code):
    """
    API para buscar detalhes de um item específico
    Uso: /api/method/erpnext.api.get_item_details?item_code=BLUSA-001
    """
    
    if not item_code:
        frappe.throw(_("Item code é obrigatório"))
    
    # Buscar item
    if not frappe.db.exists('Item', item_code):
        frappe.throw(_("Item não encontrado"))
    
    item = frappe.get_doc('Item', item_code)
    
    # Buscar estoque
    warehouse = 'Loja Brechó - GE'
    stock = frappe.db.get_value('Bin', 
        {'item_code': item_code, 'warehouse': warehouse}, 
        'actual_qty') or 0
    
    # Montar resposta
    result = {
        'item_code': item.item_code,
        'item_name': item.item_name,
        'image': item.image or '/assets/frappe/images/placeholder-image.jpg',
        'price': item.standard_rate or 0,
        'price_formatted': 'R$ %.2f' % (item.standard_rate or 0),
        'item_group': item.item_group,
        'description': item.description,
        'stock': stock,
        'tamanho': item.get('custom_tamanho'),
        'cor_principal': item.get('custom_cor_principal'),
        'estado_conservacao': item.get('custom_estado_de_conservação'),
        'marca': item.get('custom_marca_original'),
        'consignante': item.get('custom_consignante'),
        'origem': item.get('custom_origem'),
        'warehouse': warehouse
    }
    
    return result
