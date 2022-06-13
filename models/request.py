import requests

class RequestsApi(object):
    # function resultado da requisição
    def result(textSearch,limit=0):
        # ex: --> 'tv 42 polegadas'.replace(' ','+')
        try:   
            if not textSearch:             
                return 'ops. sua busca parece estar vazia!'
            else:
                textSearch = textSearch.replace(' ','+') 
                try:
                    apiRequest = f'https://api.mercadolibre.com/sites/MLB/search?q={textSearch}&limit=50&offset={limit}'
                    #print(apiRequest)
                    return requests.get(apiRequest).json()
                except Exception as e: print(e)
        except Exception as e: print(e)