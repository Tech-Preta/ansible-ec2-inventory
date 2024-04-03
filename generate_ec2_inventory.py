#!/usr/bin/env python3
import boto3
import yaml
import subprocess

def get_ec2_instances():
    # Configurar o cliente EC2
    ec2_client = boto3.client('ec2')

    # Consultar instâncias EC2 na região us-east-1 (outra região pode ser especificada)
    response = ec2_client.describe_instances()

    # Extrair informações sobre as instâncias EC2
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'instance_id': instance.get('InstanceId'),
                'private_dns_name': instance.get('PrivateDnsName'),
                'public_dns_name': instance.get('PublicDnsName'),
                'public_ip_address': instance.get('PublicIpAddress'),
                'private_ip_address': instance.get('PrivateIpAddress'),
                'tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])},
                'username': 'ec2-user',  # Substitua pelo usuário SSH desejado
                'ssh_connection': 'ssh',  # Substitua pelo tipo de conexão SSH desejado
            }
            instances.append(instance_info)
    
    return instances

def get_hostname(private_dns_name):
    try:
        result = subprocess.run(['hostname'], capture_output=True, text=True)
        current_hostname = result.stdout.strip()
        if current_hostname.startswith(private_dns_name):
            return current_hostname
        else:
            return private_dns_name
    except Exception as e:
        print("Erro ao obter o hostname:", e)
        return private_dns_name

def main():
    try:
        # Obter informações sobre as instâncias EC2
        ec2_instances = get_ec2_instances()

        # Criar estrutura de inventário YAML
        inventory = {
            'all': {
                'hosts': {}
            }
        }

        # Preencher o inventário com as informações das instâncias EC2
        for instance in ec2_instances:
            if instance['tags'].get('Name'):
                hostname = instance['tags']['Name']
            else:
                hostname = get_hostname(instance['private_dns_name'])
            inventory['all']['hosts'][hostname] = instance

        # Salvar o inventário no arquivo aws_ec2.yml
        with open('/home/nataliagranato/Documentos/Cloud/AWS/role-ec2-dynamic/inventory/aws_ec2.yml', 'w') as file:
            yaml.dump(inventory, file)
        
        print("Inventário gerado com sucesso!")

    except Exception as e:
        print("Erro ao gerar o inventário:", e)

if __name__ == '__main__':
    main()