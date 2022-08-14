from array import array
from pydoc import pager
from models.request import RequestsApi

#'https://api.mercadolibre.com/sites' lista todos os site id brasil MLB
'''

total Total de itens encontrados
offset Posição a partir da qual o item é exibido
limite Número de resultados exibidos por página limit 50!


"thumbnail": "http://http2.mlstatic.com/D_751023-MLA47083164908_082021-I.jpg",
"thumbnail_id": "751023-MLA47083164908_082021",

'''


'''
limit máximo é 50, offset vamos incrementado em 50 a cada requisição, 
usando uma regra para pegar total de paginas 50/total de paginas

exemplo:
resultado de paginas é 140 paginas
lembrando que o limit é 50 resultados por requisição

140/50 = 2.8 pagamos somente o inteiro da divisão ele vai ser nosso stop rang
a primeira requisição offset = 0 --> 0 a 50
a segunda offset = 50 --> 50 a 100
a terceira offset = 100 --> 100 a 150


limit offset = 1000
error forbidden status 403 "O deslocamento solicitado é maior que o permitido. 
O máximo permitido sem access_token é 1000
''' 

data_array = []

def format_data(data):
    l = len(data['results'])
    for i in range(0,len(data['results'])):
        data_array.append({'title': data['results'][i]['title'],
        'price': f"R$ {data['results'][i]['price']}",
        'thumbnail': data['results'][i]['thumbnail'],
        'productlink': data['results'][i]['permalink'],
        'sellername': f"{data['results'][i]['seller']['permalink']}".split('.com.br/',1)[1],
        'sellerlink': data['results'][i]['seller']['permalink']})


def result_json(textSearch):
    try:
        result = RequestsApi.result(textSearch)
        
        if type(result) is dict:
            try:
                pages = int(result['paging']['total'])//50
                if pages > 20:
                    pages = 20
                
                print(f'itens --> {result["paging"]["total"]}')
                print('')
                
                page_offset = 0
                
                for i in range(0,pages+1):
                    
                    result = RequestsApi.result(textSearch,page_offset)
                    
                    format_data(result)
                    
                    page_offset +=50
                    
                    print(f'{page_offset-50} a {page_offset} for in {i}')
                    print('')
                print(f'real get itens --> {len(data_array)}\n')
                #print(f'{data_array[0]["price"]}\n')
                print(f'{data_array[0]}\n')
                print(f'{type(data_array)}\n')
            except Exception as e: print(e)
        else:
            print(result)
    except Exception as e: print(e)

def export_array():
    return data_array

