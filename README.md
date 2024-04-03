# Script de Geração de Inventário AWS EC2

Este script em Python foi desenvolvido para automatizar a geração de um inventário YAML das instâncias EC2 em uma conta da AWS.

## Pré-requisitos

- Python 3.x instalado no ambiente.
- Biblioteca boto3 para Python instalada (`pip install boto3`).
- Acesso às instâncias EC2 na conta da AWS.
- Permissões IAM adequadas para consultar instâncias EC2.

## Funcionalidades

- Consulta as instâncias EC2 em uma determinada região (us-east-1 por padrão).
- Extrai informações relevantes das instâncias EC2, como IDs, nomes, endereços IP, etc.
- Cria um inventário YAML com os detalhes das instâncias EC2.
- Pode ser configurado para usar um usuário SSH específico e um tipo de conexão SSH desejado.

## Uso

1. Certifique-se de ter configurado corretamente suas credenciais AWS.
2. Execute o script `generate_ec2_inventory.py`.
3. Verifique o arquivo `aws_ec2.yml` gerado no diretório especificado.

## Configuração

Antes de executar o script, certifique-se de revisar e ajustar as seguintes configurações conforme necessário:

- **Usuário SSH**: Substitua `'ec2-user'` pelo nome do usuário SSH desejado.
- **Tipo de Conexão SSH**: Substitua `'ssh'` pelo tipo de conexão SSH desejado.
- **Local de Salvamento do Inventário**: Ajuste o caminho do arquivo de inventário YAML conforme desejado.

## Observações

- Este script foi desenvolvido para uso em ambientes Linux/Unix.
- Certifique-se de ter as permissões adequadas para executar o script e gravar o inventário no diretório especificado.

## Autor

Este script foi desenvolvido por Natalia Granato. Para feedback ou contribuições, entre em contato.

