# Perguntas
## 1) Você acha que este código está estruturado, legível e escalável?

Não, esta com todos os arquivos juntos e misturados. Pode haver uma reestruturação!

## 2) O que você mudaria nos arquivos e na estrutura de pastas para melhorá-lo nesse sentido?

Flask -> |-APP
         |--SERVER 
         |--Routes
         |--CONFIGS
         

## 3) Quanto a arquitetura API e sua conteinerização, liste as brechas de segurança que você identificou neste código?

Estamos definindo diretamente a senha/usuario no codigo versionado do banco
def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")

    

## 4) Como você as resolveria?

Colocar ele em uma outra file, e não deixar versionar essa outra file.
