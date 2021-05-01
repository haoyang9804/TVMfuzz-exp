#calculate the correlation

library(ggplot2)
library(readxl)
library(plyr)
library(lattice)
library(Rmisc)
library(scales)
library(corrplot)

bugs <-  read_excel(path = '../labeled_dataset.xlsx', sheet="ALL")
tvm_bugs = subset(bugs, project=="TVM")
glow_bugs = subset(bugs, project=="Glow")
ngraph_bugs = subset(bugs, project=="nGraph")
bugs_number = as.vector(table(bugs$project))
bugs_number = c()
bugs_number[1:12] <- as.vector(table(bugs$project))[1]  # 12 categories of root causes, including: other
bugs_number[13:24] <- as.vector(table(bugs$project))[2]
bugs_number[25:36] <- as.vector(table(bugs$project))[3]

row_name <- c("TVM", "Glow", "nGraph")
########################## root causes ##########################
a <- table(bugs$`root causes`, bugs$project)
a <- a/bugs_number
glow_ <- a[1:12]
ngraph_ <- a[13:24]
tvm_ <- a[25:36]

cor_tvm_glow_causes <- cor(glow_,tvm_, method = "spearman")    
cor_tvm_ngraph_causes <- cor(tvm_,ngraph_,method = "spearman")    
cor_glow_ngraph_causes <- cor(ngraph_,glow_,method = "spearman")  

res_causes <- c(1, cor_tvm_glow_causes, cor_tvm_ngraph_causes, 
                cor_tvm_glow_causes, 1, cor_glow_ngraph_causes, 
                cor_tvm_ngraph_causes, cor_glow_ngraph_causes, 1)

my_color <- c()
my_color[1:16] <- "grey"
#my_color[17:20] <- c("#E6F5D0","#B8E186","#7FBC41","#4D9221") # green!!!!!!
my_color[17:20]<- c("white","#9ECAE1","#438DC3","#3182BD") #blue !!!


col_my=colorRampPalette(my_color)

res_cor <- matrix(data=res_causes, nrow = 3, ncol = 3, dimnames = list(row_name, row_name))
p1 <- corrplot::corrplot(corr=res_cor,
                         method = "color",
                         order = "AOE",
                         col = col_my(400),
                         addCoef.col = "black",
                         type = "lower",
                         diag=T,
                         bg="white",
                         outline=TRUE,
                         rect.col="blue",
                         number.cex=1.1,
                         
                         tl.srt = 0, 
                         tl.offset=1, 
                         tl.pos = "ld",
                         tl.col="black",
                         tl.cex = 1.2,
                         
                         cl.lim = c(.7, 1),
                         cl.pos = "b", # legend in the bottom
                         cl.ratio = .3, # legend width
                         #cl.align.text = "l",
                         cl.length=4,
                         cl.cex = 1,)
p1

###################### symptoms ####################################
b <- table(bugs$`symptoms`, bugs$project)
# b <- b/bugs_number
glow_symptoms <- b[1:6]
ngraph_symptoms <- b[7:12]
tvm_symptoms <- b[13:18]


cor_tvm_glow_sym <- cor(glow_symptoms,tvm_symptoms, method = "spearman")    
cor_tvm_ngraph_sym <- cor(tvm_symptoms,ngraph_symptoms,method = "spearman")   
cor_glow_ngraph_sym <- cor(ngraph_symptoms,glow_symptoms,method = "spearman")  

res <- c(1, cor_tvm_glow_sym, cor_tvm_ngraph_sym, 
         cor_tvm_glow_sym, 1, cor_glow_ngraph_sym, 
         cor_tvm_ngraph_sym, cor_glow_ngraph_sym, 1)


res_cor <- matrix(data=res, nrow = 3, ncol = 3, dimnames = list(row_name, row_name))


p1 <- corrplot::corrplot(corr=res_cor,
                         method = "color",
                         order = "AOE",
                         col = col_my(400),
                         addCoef.col = "black",
                         type = "lower",
                         diag=T,
                         bg="white",
                         outline=TRUE,
                         rect.col="blue",
                         number.cex=1.1,
                         
                         tl.srt = 0, 
                         tl.offset=1, 
                         tl.pos = "ld",
                         tl.col="black",
                         tl.cex = 1.2,
                         
                         cl.lim = c(.7, 1),
                         cl.pos = "b", # legend in the right
                         cl.ratio = .3, # legend width
                         #cl.align.text = "l",
                         
                         cl.length=4,
                         cl.cex = 1,)
p1

