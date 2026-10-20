# Préparation de la VM Docker par Ansible
**Uniquement sur VM de laboratoire avec accord d'administration.** Les commandes exécutées avec become modifient la VM ciblée ; ne jamais lancer sur l'hyperviseur Proxmox ni sur un serveur de mairie non autorisé.

## Pré-requis
- 1 VM Debian lab avec SSH + compte autorisé sudo.
- Ansible sur votre poste de gestion.
- Vérifier le nom du paquet Docker Compose disponible pour votre version de Debian ; le playbook utilise docker-compose-v2 de la distribution.
- Adapter la cible dans une copie privée de hosts.example.ini.

## Prévisualisation
    ansible-playbook -i infra/ansible/hosts.example.ini infra/ansible/install-staging.yml --check --diff

## Exécution (après validation)
    ansible-playbook -i infra/ansible/hosts.example.ini infra/ansible/install-staging.yml --become --ask-become-pass

La VM reçoit Docker Engine/Compose et /opt/muni-cloud/compose.staging.yaml ; le service applicatif **n'est pas déployé automatiquement** par Ansible et la VM ne sera pas ouverte au public. Tester d'abord dans une VM jetable snapshotée.
