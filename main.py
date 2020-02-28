from git import Repo

# rarepo é um Repo instanciado apontando para o repositório do git-python
# Para o começo, o primeiro argumento para Repo é o caminho para o repositório
# que você quer trabalhar

repo = Repo(path="/Users/IgorPompeoTavares/Desktop/Igor/AutoPy/.git")
assert not repo.bare

repo.config_reader()           # pega a configuração de leitura para acesso de apenas leitura
with repo.config_writer():     # pega a configuração de escrita para mudar a configuração
    pass                       # chama release() para ter certeza que as alterações estão escritas e bloqueadas são liberadas

assert not repo.is_dirty()     # valida o status sujo
repo.untracked_files           # recebe uma lista de arquivos de não rastreados
# ['my_untracked_file']
