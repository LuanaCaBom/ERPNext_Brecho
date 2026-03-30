
<div style="padding: 20px; font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 5px;">
    <div style="background-color: #4CAF50; padding: 15px; border-radius: 5px 5px 0 0;">
        <h2 style="color: white; margin: 0;"> Novo Consignante Cadastrado</h2>
    </div>
    
    <div style="padding: 20px;">
        <p style="font-size: 16px;">Um novo consignante foi cadastrado no sistema:</p>
        
        <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
            <tr>
                <td style="padding: 10px; background-color: #f5f5f5; width: 120px;"><strong>Nome:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #e0e0e0;">{{ doc.customer_name }}</td>
            </tr>
            <tr>
                <td style="padding: 10px; background-color: #f5f5f5;"><strong>Email:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #e0e0e0;">{{ doc.email_id or "Não informado" }}</td>
            </tr>
            <tr>
                <td style="padding: 10px; background-color: #f5f5f5;"><strong>Telefone:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #e0e0e0;">{{ doc.mobile_no or "Não informado" }}</td>
            </tr>
            <tr>
                <td style="padding: 10px; background-color: #f5f5f5;"><strong>Grupo:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #e0e0e0;">{{ doc.customer_group }}</td>
            </tr>
        </table>
        
        <p style="margin-top: 20px;">
            <a href="/app/customer/{{ doc.name }}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 3px; display: inline-block;">🔍 Ver Detalhes no Sistema</a>
        </p>
        
        <p style="color: #666; font-size: 12px; margin-top: 30px;">
            Este é um email automático do sistema ERPNext - Brechó Estilo Único
        </p>
    </div>
</div>
