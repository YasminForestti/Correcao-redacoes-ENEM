import uol_redacoes_xml
essays = uol_redacoes_xml.load()

print(essays[1].criteria_scores)
# texto original da primeira redação

# print([attr for attr in essays[0].__dir__() if not attr.startswith('_')])
# # exibe os atributos do objeto de redação (exceto os privados, que começam com '_')