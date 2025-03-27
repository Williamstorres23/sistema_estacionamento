# Usa a imagem oficial do Nginx como base
FROM nginx:alpine

# Define o diretório de trabalho
WORKDIR /usr/share/nginx/html

# Remove arquivos padrão do Nginx
RUN rm -rf ./*

# Copia todos os arquivos do frontend para o container
COPY . .

# Expõe a porta 80 para acesso ao site
EXPOSE 80

# Comando padrão do Nginx para rodar
CMD ["nginx", "-g", "daemon off;"]
