import glob 
import cv2
import skimage
from skimage.io import imread, imsave
from skimage.io import imread_collection
from skimage.filters import threshold_otsu, sobel  
from skimage.color import rgb2gray 
from matplotlib import pyplot as plt
from skimage import exposure, filters
import os

class Filters():

    '''
    Aplica  5 filtros em uma pasta de imagens, transforma as imagens de uma pasta em um canal
    do tipo luv, e aplica o canal u do luv, o filtro gaussiano e o clahe de uma só vez. Os filtros são:
    gray, gaussiano, chahe, equalizaçao de histograma e extração de bordas

    Parêmetros
    ==========
    images : str 
        Endereço da pasta que contém as imagens

    format : str
        extenção das imagens que serão trabalhadas

    '''


    def __init__(self, images = None, format = "jpg"):
        self.images = images
        self.format = format


    def rename_file(self, file):

        '''
        Esta função é responsável por retornar uma string contendo o nome do arquivo a partir do '\'
        é feito esse método para axiliar na hora da escrita dos arquivos

        Parâmetros
        ==========

        file: str
            Endereço de uma imagem que está contida em uma pasta 

        Returns
        =======

        output : str
            Endereço até o '\'

        '''

        
        output = None
        if('\\' in file):

            indice = 0

            while True:
                
                try:
                    aux = file.index('\\', indice+1)
                except:
                    break
                indice = aux
            output = file[indice + 1:]

        return output



    def filter_gray_all(self, folder = None):


        '''
        Esta função é responsável por gerar uma pasta contendo contendo as imagens de entrada em imagens em tom de cinza

        Parâmetros
        ==========

        folder: str
            Endereço da pasta na qual o usuário deseja salvar as imagens processadas 

        Returns
        =======

        imagens_transform : list
            Além do código salvar as imagens em uma pasta, ele retorna uma lista contendo todas as imagens processadas 

        '''


        if not os.path.exists(folder):
            os.makedirs(folder)

        images_all = glob.glob(self.images + '/*.' + self.format)
        
        images_transform = []
        for i in images_all:
            image = imread(i)
            output = self.rename_file(i)
            image = rgb2gray(image)
            images_transform.append(image)
            folder_aux = folder + '\\Gray_' + output
            print(folder_aux)
            imsave(folder_aux, image)
        return images_transform


    def filter_gaussiano_all(self, kernel = 3, folder = None):

        '''
        Esta função é responsável por gerar uma pasta contendo contendo as imagens de entrada em imagens 
        com o filtro gaussiano, que é usado para reduzir o nível de ruído de um sinal de entrada 

        Parâmetros
        ==========

        kernel : int
            ajustar a regulagem do desfoque

        folder : srt
            Endereço da pasta na qual o usuário deseja salvar as imagens processadas 
        
        Returns
        =======

        imagens_transform : list
            O método retorn a uma lista contendo todas as imagens já pré-processadas

        '''
        
        if not os.path.exists(folder):
            os.makedirs(folder)

        images_all = glob.glob(self.images + '/*.' + self.format)
        

        images_transform = []

        for i in images_all:
            image = imread(i)
            output = self.rename_file(i)
            image = cv2.GaussianBlur(image,(kernel, kernel),cv2.BORDER_DEFAULT)
            images_transform.append(image)
            folder_aux = folder + '\\Gaussiano_' + output
            print(folder_aux)
            imsave(folder_aux, image)
        
        return images_transform


    def filter_clahe_all(self, kernel_size=127, nbins=256, folder = None):

        '''
        Esta função gera uma pasta contendo imagens com a aplicação do filtro clahe para o 
        para o aumento de contraste das imagens  

        Parâmetros
        ==========

        folder : str
            string responsável por definiar a pasta das imagens que seram salvas
        
        kernel_size : int
            Representa o tamanho da janela   para aplicar  filtro

        nbins : int


        Returns
        =======

        imagens_transform : list
            Retorna uma lista com as imagens com o clahe aplicado

        '''
        

        if not os.path.exists(folder):
            os.makedirs(folder)
        
        images_all = glob.glob(self.images + '/*.' + self.format)
        

        images_transform = []

        for i in images_all:
            image = imread(i)
            output = self.rename_file(i)
            image = skimage.exposure.equalize_adapthist(image, kernel_size = kernel_size, nbins = nbins)
            images_transform.append(image)
            folder_aux = folder + '\\Clahe_' + output
            print(folder_aux)
            imsave(folder_aux, image)
        
        return images_transform


    def filter_EqHist_all(self, folder = None):


        '''
        O método aplica a equalalização de histograma nas imagens, nal qual sua função é 
        mudar a distribuição dos valores de ocorrência em um histograma permitindouma redução
        das diferenças acentuadas, gerando uma pasta com todas as imagens processadas

        Parâmetros
        ==========

        folder : str
            Variável resposável para saber o novo enderenço da pasta, ou a alocação das imagens em uma pasta 
            ja existente
        
        Returns
        =======

        imagens_transform : list
            Retorna uma lista com as imagens o fittro de equalização de histograma

        '''
        

        if not os.path.exists(folder):
            os.makedirs(folder)

        images_all = glob.glob(self.images + '/*.' + self.format)
        

        images_transform = []

        for i in images_all:
            image = imread(i)
            output = self.rename_file(i)
            image = skimage.exposure.equalize_hist(image)
            images_transform.append(image)
            folder_aux = folder + '\\EqHist_' + output
            print(folder_aux)
            imsave(folder_aux, image)
            
        
        return images_transform


    def filter_edge_all(self, folder = None):

        '''

        O método filter_edge_all aplicaca processamentos nas imagens de entrada para extrair ar bordas
        que contem na imagem, salvando elas em uma pasta
        

        Parâmetros
        ==========

        folder : str
            Nome da pasta na qual o usuário deseja salavar as novas imagens
        
        Returns
        =======

        imagens_transform : list
            Retorna uma lista a aplicação do filtro


        '''



        if not os.path.exists(folder):
            os.makedirs(folder)

        images_all = glob.glob(self.images + '/*.' + self.format)
    

        images_transform = []

        for i in images_all:
            image = imread(i)
            output = self.rename_file(i)
            image =  rgb2gray(image)
            otsu = threshold_otsu(image)
            blanck_and_whithe = (image < otsu)
            sobel_aux = sobel(blanck_and_whithe)
            images_transform.append(sobel_aux)
            folder_aux = folder + '\\Edge_' + output
            print(folder_aux)
            imsave(folder_aux, sobel_aux)
        
        return images_transform


    def transform_luv(self, l = False, u = False, v = False, folder = None):

        '''

        Esse método transforma uma imagem em qualquer canal do tipo, luv, podendo extrair o canal l, u ou o v
        colocandoas em uma nova pasta
        

        Parâmetros
        ==========

        l : boll
            Variável será True caso o usuário queira transformar as imagens para o canal l, caso contrário
            ela deverá iniciar com False

        u : boll
            Variável será True caso o usuário queira transformar as imagens para o canal, caso contrário
            ela deverá iniciar com False
 
        
        v : boll
            Variável será True caso o usuário queira transformar as imagens para o canal v, caso contrário
            ela deverá iniciar com False


        folder : str
            variável que representa a nova pasta para a alocação das imagens


        
        Returns
        =======

        imagens_transform : list
            Retorna uma lista das imagens de um um canal escolhida pelo usuário


        '''


        if not os.path.exists(folder):
            os.makedirs(folder)

        images_all = glob.glob(self.images + '/*.' + self.format)

        images_transform = []

        if l:
            for i in images_all:
                image = cv2.imread(i)
                output = self.rename_file(i)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
                l,u,v = cv2.split(image)
                l = (l).astype('uint8')
                images_transform.append(l)
                folder_aux = folder + '\\luv_l_' + output
                print(folder_aux)
                imsave(folder_aux, l)
            
            return images_transform

        if u:
            for i in images_all:
                image = cv2.imread(i)
                output = self.rename_file(i)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
                l,u,v = cv2.split(image)
                u = (u).astype('uint8')
                images_transform.append(u)
                folder_aux = folder + '\\luv_u_' + output
                print(folder_aux)
                imsave(folder_aux, u)
            
            return images_transform

        if v:
            for i in images_all:
                image = cv2.imread(i)
                output = self.rename_file(i)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
                l,u,v = cv2.split(image)
                v = (v).astype('uint8')
                images_transform.append(v)
                folder_aux = folder + '\\luv_v_' + output
                print(folder_aux)
                imsave(folder_aux, v)
            
            return images_transform

    def transform_ugc(self,folder = None, kernel = 3,kernel_size = 127 ,nbins = 256):

        '''

        O método aplica o 3 métodos de uma vez nas imagens de uma pasta, o canal u de luv, o filtro gaussiano
        e o clahe
        

        Parâmetros
        ==========

        folder : str
            Nome da pasta na qual o usuário deseja salavar as novas imagens

        kernel : int
            ajuste de desfoque no filtro gaussiano

        kernel_size : int
            Representa o tamanho da janela   para aplicar  filtro no clahe

        nbins : int
            ajuste para o clahe

        Returns
        =======

        imagens_transform : list
            Retorna uma lista a aplicação do canal de cor e os 2 filtros


        '''

        
        if not os.path.exists(folder):
            os.makedirs(folder)

        images_all = glob.glob(self.images + '/*.' + self.format)

        images_transform = []

        for i in images_all:
            
            image = cv2.imread(i)
            output = self.rename_file(i)
            image = cv2.cvtColor(image , cv2.COLOR_BGR2LUV)
            l,u,v = cv2.split(image)
            u =  cv2.GaussianBlur(u,( kernel, kernel ),cv2.BORDER_DEFAULT)
            u = (u).astype('uint8')
            u = skimage.exposure.equalize_adapthist(u, kernel_size = kernel_size, nbins = nbins)
            images_transform.append(u)
            folder_aux = folder + '\\ugc_' + output
            print(folder_aux)
            imsave(folder_aux, u)
            
        
        return images_transform


    

class Filters_uniq():

    def __init__(self):
        pass

    '''
    Nessa secção os métodos serão para uso rápido e prático, onde não é preciso utilizar nenhum paramentro no contrutor
    seus métodos são os mesmo das funções na classe Filters, porém aplicados a uma só imagem

    '''
        
    def filter_gray(self, image):

        '''

        Transforma uma imagem para cinza

        Parêmetros
        ==========
        image : str 
            Endereço da imagem que o usário deseja fazer a transição

        Returns
        =======

        image : float
            Como é feita a leitura da imagem dentro da função, é retornada ela mesma já lida e com o filtro aplicado

        '''

        image = imread(image)
        image = rgb2gray(image)

        return image


    def filter_gaussiano(self, image, kernel = 3):

        '''

        Aplica o filtro gaussiano em uma imagem

        Parêmetros
        ==========

        image : str 
            Endereço da imagem que o usário deseja fazer a transição
        
        kernel : int
            ajuste do desfoque
        

        Returns
        =======

        image : float
            Como é feita a leitura da imagem dentro da função, é retornada ela mesma já lida e com o filtro aplicado

        '''

        image = imread(image)
        image = cv2.GaussianBlur(image,( kernel, kernel ),cv2.BORDER_DEFAULT)

        return image

    def filter_clahe(self, image,kernel_size=127, nbins=256):

        '''

        Aplica o filtro clahe em uma imagem

        Parêmetros
        ==========

        image : str 
            Endereço da imagem que o usário deseja fazer a transição
        
        kernel_size: int
             Representa o tamanho da janela   para aplicar  filtro

        nbins : int

        Returns
        =======

        image : float
            Como é feita a leitura da imagem dentro da função, é retornada ela mesma já lida e com o filtro aplicado


        '''
        image = imread(image)
        image = skimage.exposure.equalize_adapthist(image, kernel_size,nbins)

        return image

    def filter_EqHist(self, image):

        '''

        Aplica a equalização de histograma em uma imagem

        Parêmetros
        ==========

        image : str 
            Endereço da imagem que o usário deseja fazer a transição

        Returns
        =======

        image : float
            Como é feita a leitura da imagem dentro da função, é retornada ela mesma já lida e com o filtro aplicado

        '''


        image = imread(image)
        image = skimage.exposure.equalize_hist(image)

        return image
    
    def filter_edge(self, image):

        '''

        Aplica o filtro para devolver as bordas de uma imagem

        Parêmetros
        ==========
        
        image : str 
            Endereço da imagem que o usário deseja fazer a transição

        Returns
        =======

        image : float
            Como é feita a leitura da imagem dentro da função, é retornada ela mesma já lida e com o filtro aplicado

        '''

        image = imread(image)
        image =  rgb2gray(image)
        otsu = threshold_otsu(image)
        blanck_and_whithe = (image < otsu)
        sobel_aux = sobel(blanck_and_whithe)
        
       
        return sobel_aux

    def channel_luv(self, image, l = False, u = False, v = False):


        '''

        Transforma uma imagem em qualquer um canal do sistema de cor luv

        Parêmetros
        ==========
        
        image : str 
            Endereço da imagem que o usário deseja fazer a transição
        
        l : bool
            True caso o usuário queira a imagem com o filtro l, caso contrário deverá ser False

        u : bool
            True caso o usuário queira a imagem com o filtro u, caso contrário deverá ser False

        v : bool
            True caso o usuário queira a imagem com o filtro v, caso contrário deverá ser False

        Returns
        =======

        image : float
            Como é feita a leitura da imagem dentro da função, é retornada ela mesma já lida e com a transição aplicada

        '''
        image = imread(image)
        image = cv2.cvtColor(image , cv2.COLOR_BGR2LUV)
        l,u,v = cv2.split(image)

        if l:
            l = (l).astype('uint8')
            return l
        if u:
            u = (u).astype('uint8')
            return u
        if v:
            v = (v).astype('uint8')
            return v



    def plot_hists(self, images1):

        type(images1)

        '''

        Ver gráfico de histograma de uma imagem

        Parêmetros
        ==========
        
        images1 : float 
            Entrada com uma foto já lida
    '''

        plt.hist(images1.ravel(), bins=100, density=True, color='b', alpha=1)
            
        plt.show()