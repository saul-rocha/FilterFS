*****
filterFS
*****

Esse é um pacote que modifica imagens rgb para canais de imagens LUV, aplica os filtros gray, gaussiano, clahe, equalização de histograma e bordas de objetos nas imagens em uma determianda pasta com N imagens.


Instalação:
####
 pip install filtersFS

Usos:
####
Exemplos::
    from filtersFS import Filters, Filters_uniq

    data_set = Filters('../imgs','jpg')



    data_gray = []
    data_gray = data_set.filter_gray_all('pasta_gray')

    data_gaussiano = []
    data_gaussiano = data_set.filter_gaussiano_all(sigmaradius = 3.0, 'pasta_gau')

    data_clahe = []
    data_clahe = data_set.filter_clahe_all(kernel_size=127, nbins=256, 'pasta_clahe')

    data_eqHist = []
    data_eqHist = data_set.filter_EqHist_all('pasta_EqHist')

    data_edge = []
    data_edge = data_set.filter_edge_all('pasta_edge')

    data_luv = []
    l = False
    u = True
    v = False
    data_luv = data_set.transform_luv(l, u, v, 'pasta_luv')

    data_ugc = []
    data_ugc = data_set.transform_ugc('pasta_ugc',3.0,127,256)


    nome_filtro (filter_edge, filter_gray, filter_clahe, filter_gaussiano, channel_luv(bool, boll, bool), filter_Eq_Hist)

    data_set1 = Filters_uniq()
    res = data_set1.nome_filtro('../diretorio/img.jpg') 