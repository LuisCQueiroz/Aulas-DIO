# Funções
# Fazem parte de um pacote
# Pacotes contém muitas funções e precisam ser instalados.
# Não sendo um pacote padrão, ele precisa ser instalado.

a <- "Heitor"
b <- "João"
c <- c(a,b)
c

# Help
?c

c <- c("Heitor", "João")
c

a <- c(10,5,15,20)
a[1] # Apresenta o primeiro elemento da lista
a

# Apresenta (Min, Primeiro Quartil, Mediana,  Média, terceiro Quartil, Máximo) 
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
?summary
summary(a)
summary(c)

# função de pacote não padrão
# Para saber qual pacote deverá instalar
# Acessar https://rdocumentation.org

# Instalando o pacote stringr
?str_c
install.packages("stringr")
library(stringr)

Nome <- "João"
Sobrenome <- "Silva"
library(stringr)
NomeCompleto <- str_c(Nome, Sobrenome)
NomeCompleto
NomeCompleto <- str_c(Nome, " ", Sobrenome)
NomeCompleto

