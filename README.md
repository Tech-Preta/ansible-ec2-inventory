# ansible-ec2-inventory
# Projeto Ansible para Descoberta de Instâncias AWS e Configuração SSH

Este projeto Ansible descobre instâncias EC2 na AWS e configura a chave SSH do host controlador nas instâncias descobertas.

## Estrutura do Projeto

├── ansible.cfg
├── inventory
│   ├── ec2.py
│   └── ec2.ini
├── roles
│   └── aws_discovery
│       ├── tasks
│       │   └── main.yml
│       └── vars
│           └── main.yml
├── playbook.yml
└── test.yml

## Pré-requisitos

- Ansible 2.9 ou superior
- Python 3.6 ou superior
- boto3 (Python SDK da AWS)
- Uma chave SSH configurada no seu host controlador

## Configuração

1. Atualize o arquivo `ansible.cfg` com suas informações de chave privada SSH e usuário remoto.
2. Configure suas credenciais da AWS. Você pode fazer isso configurando as variáveis de ambiente `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` e `AWS_REGION`, ou usando o comando `aws configure` do AWS CLI.
3. Atualize o caminho para a sua chave pública SSH no arquivo `roles/aws_discovery/vars/main.yml`.

## Execução

Para executar o playbook, use o seguinte comando:

```bash
ansible-playbook playbook.yml
```
Após a execução do playbook, você pode verificar se a chave SSH foi copiada corretamente para as instâncias descobertas executando o teste:

```
ansible-playbook test.yml
```

## Contribuição
Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar uma solicitação pull.