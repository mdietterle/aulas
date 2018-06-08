import io

import requests
import requests_cache
import rows
import openpyxl
#import rows.plugins.xlsx

plugin_name = 'xlsx'
file_extension = 'xlsx'
field_names = ('txNomeParlamentar, idecadastro, nuCarteiraParlamentar, nuLegislatura, sgUF, sgPartido, '
                'codLegislatura, numSubCota, txtDescricao, '
                'numEspecificacaoSubCota, txtDescricaoEspecificacao, '
                'txtFornecedor, txtCNPJCPF, '
                'txtNumero, indTipoDocumento, '
                'datEmissao, vlrDocumento, vlrGlosa, vlrLiquido, numMes, numAno, numParcela, '
                'txtPassageiro, txtTrecho, numLote, numRessarcimento, vlrRestituicao, nuDeputadoId'
                'ideDocumento, ').split(', ')
for field_name in field_names:
    if field_name in ('txNomeParlamentar', 'sgUF', 'sgPartido', 'txtDescricao', 'txtDescricaoEspecificacao', 'txtFornecedor'):
        field_type = rows.fields.TextField
    else:
        field_type = rows.fields.DecimalField
    FIELDS[field_name] = field_type
requests_cache.install_cache('olimpiadas')
url = 'http://www.camara.leg.br/cotas/Ano-2017.xlsx'
response = requests.get(url)
book = openpyxl.load_workbook(filename, data_only=True)
sheet = book['Contracheque']
table = rows.import_from_xlsx
#inicio duvida
metadata = extract_metadata(filename)
metadata['url'] = link.url
metadata['tribunal'] = link.name
start_row = metadata.pop('start_row')

result = []
table = import_function(
        str(filename),
        start_row=start_row,
        fields=FIELDS,
        skip_header=False,
    )
for row in table:
    row_data = row._asdict()
    if is_filled(row_data):
        result.append(convert_row(row_data, metadata))


#final duvida

#inicio duvida



#final duvida

rows.export_to_csv(table, 'cotas_deputados.csv')