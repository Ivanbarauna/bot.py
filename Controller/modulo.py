import os
import random
import discord
# clase responsável por gerenciar as imagens
class ImageManager:
    # pasta onde as imagens estão armazenadas
    img_folder = "img"
    # Tipos de arquivos aceitos como  imagens
    validation = [".png", ".jpg", ".jpeg", ".gif"]
    
    @classmethod
    # Retorna a lista de imagens válidas da pasta 'img
    def get_images(cls):
        if not os.path.exists(cls.img_folder):
            return [] # Se a pasta não existir, retorna lista vazia
        return [f for f in os.listdir(cls.img_folder) 
                if f.lower().endswith(tuple(cls.validation))]
        
    @classmethod
    # Procura uma imagem pelo nome dentro da pasta. Se não encontrar, retorna None
    def find_image(cls, name=None):
        images = cls.get_images()
        for img in images:
            if name and name.lower() in img.lower():
                return img # Retorna a imagem encontrada
        return None  # Agora só retorna None se não encontrar
        
    @classmethod
    # Retorna o caminho completo da imagem
    def get_path(cls, name=None):
        image = cls.find_image(name)
        return os.path.join(cls.img_folder, image) if image else None
# cria o embed do discord com o título, descrição, imagem e (se existir) 
def create_embed(title, description, image_path, color=None):
    embed = discord.Embed(title=title, description=description ,color=color)
    # tenta encontrar a imagem correspondente
    image = ImageManager.find_image(image_path)
    if image:
        path = ImageManager.get_path(image_path)
        # prepara o arquivo para envio
        file = discord.File(path)
        embed.set_image(url=f"attachment://{image}") # anexa a imagem ao embed
        return embed, file
    else:
    # se não encontrar a imagem, adiciona um aviso no embed
        embed.add_field(name=" Aviso", value="Imagem não encontrada.", inline=False)
    
    return embed, None
#  cria o embed que mostra todas as imagens disponíveis na pasta img
def gallery_embed():
    images = ImageManager.get_images()
    embed = discord.Embed(title="Galeria de Imagens", color=discord.Color.blue())
    
    if images: 
    # lista todas as imagens disponíveis
        image_list = "\n".join(f"- {img}" for img in images)
        embed.add_field(name="Imagens Disponíveis", value=image_list, inline=False)
    else:
        # caso não haja imagens na pasta
        embed.description = "Nenhuma imagem disponível."
        
    return embed
