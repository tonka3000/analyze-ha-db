cd /workspace

pip install cryptography
echo "Enter your backup password for '$HA_BACKUP_TAR_FILENAME':"
read -s password
python secure_tar.py "$HA_BACKUP_TAR_FILENAME" -p "$password" --filter "homeassistant.tar.gz"
