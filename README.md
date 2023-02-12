## projeto estudo 📚 API mercado livre 
##
## Relatório Preço Mínimo Anunciado (PMA)
## author ⛏  https://github.com/renanrrodrigues

## lib
- [requests](https://pypi.org/project/requests/) - 2.28.0
- [json](https://pypi.org/project/jsonlib/) - 1.6.1
- [openpyxl](https://pypi.org/project/openpyxl/) - 3.0.10


## Features
- ⚠️ offset limit de 1000 acesso sem token
- ⚠️ a API tem limit de 50 resultados por requisição
- ✅ percorrer todas as 20 paginas 20*50 = 1000
- ✅ montar um array ou dict com os seguintes itens
    - ✅ titulo do produto
    - ✅ preço
    - ✅ foto da capa
    - ✅ link do produto
    - ✅ nome do vendedor
    - ✅ url do vendedor
- ✅ save csv ou json
- ✅ gerar um relatório em excel

## Json

```JSON
{
    "title": "Smart Tv 42' Led Fhd Ptv42g52 Com Roku Dolby Áudio Philco", 
    "price": "R$ 1899",
    "thumbnail": "http://http2.mlstatic.com/D_716662-MLB46652836450_072021-I.jpg",
    "productLink": "https://produto.mercadolivre.com.br/MLB-1836205903-smart-tv-42-led-fhd-ptv42g52-com-roku-dolby-audio-philco-_JM", 
    "sellerName": "MERCADOLIVRE+ELETRONICOS", 
    "sellerLink": "http://perfil.mercadolivre.com.br/MERCADOLIVRE+ELETRONICOS"
}
```


✅ concluído
❌ não concluído
