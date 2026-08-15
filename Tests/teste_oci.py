import oci

config = oci.config.from_file()

print("Configuração OCI carregada com sucesso!")
print("Região:", config["region"])