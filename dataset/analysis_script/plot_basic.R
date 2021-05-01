library(ggplot2)
library(readxl)
library(plyr)
library(lattice)
library(Rmisc)
library(scales)
library(cowplot)
library(patchwork)

bugs <-  read_excel(path = '../labeled_dataset.xlsx', sheet="ALL")
bugs$project=factor(bugs$project, levels = c("TVM","Glow","nGraph"))
#bugs$`root causes` = factor(bugs$`root causes`, levels = c("Crash","Wrong Code","Bad Performance","Hang","Build Failure","Unreported"))
tvm_bugs = subset(bugs, project=="TVM")
glow_bugs = subset(bugs, project=="Glow")
ngraph_bugs = subset(bugs, project=="nGraph")
bugs_number = as.vector(table(bugs$project))
bugs_number = c()
bugs_number[1:6] <- 318  # tvm
bugs_number[7:12] <- 145  #glow
bugs_number[13:17] <- 140 # nGraph no hang

#sym_palette <- c("#FDAE61","#FEDF90","#DDEEF4","#ACD9E9","#74ADD1","#4575B4")
#sym_palette <- rev(sym_palette)
sym_palette <- c("#F4ACB7","#FFD3DB","#DDEEF4","#ACD9E9","#74ADD1","#4575B4") 
sym_palette <- rev(sym_palette)

my_axis_size <- 9.5
my_title_size <- 12
my_legend_size <- 9.5
my_axis_color="black"
# plot symptoms
p <- ggplot(bugs, aes(x = project,fill=symptoms))
p + geom_bar(position = "fill", width = 0.7, alpha=0.95) + 
  xlab("") + 
  ylab("") +
  scale_fill_manual(values=sym_palette, 
                    #breaks = c("Crash","Wrong Code","Bad Performance","Hang","Build Failure","Unreported")
                    )+
  theme(legend.title=element_blank(), 
        legend.position = "right",
        legend.text = element_text(size = 9),
        panel.background = element_rect(fill = "#efefef"), 
        axis.text =element_text(face = "bold",
                                size = my_axis_size, 
                                colour = my_axis_color,)) +
  geom_text(aes(label=paste(round(..count.. / bugs_number ,4 )*100 , "%", sep = '')),
  #geom_text(aes(label=..count..),          
            stat = 'count',size=4,position = position_fill(vjust = 0.5)) +
  scale_y_continuous(labels=percent) 

ggsave("symptom.pdf")

# plot root causes_stack


# order in my order
causes_data <- table(bugs$`root causes`)
causes_data <- sort(causes_data, decreasing = F)
causes_name <- as.data.frame(causes_data)$Var1
causes_name <- as.array(causes_name)

bugs$`root causes` = factor(bugs$`root causes`, levels = causes_name)


#causes_palette <- c("#7BDFF2","#06AED5","#1985A1") 
#causes_palette <- c("#B8E186","#7FBC41","#4D9221") #green !!!!


causes_palette <- c("#D2E6F1","#9ECAE1","#3182BD") #blue 
bugs$project=factor(bugs$project, levels = c("nGraph","Glow","TVM"))
p <- ggplot(bugs, aes(y=`root causes`, fill = project))
p + geom_bar( alpha = 0.9) + 
  xlab("") + 
  ylab("") + 
  scale_fill_manual(values = causes_palette, guide = guide_legend(reverse=TRUE))+
  theme(panel.background = element_rect(fill = "#efefef")
        ,axis.text = element_text( face="bold", 
                                  size = my_axis_size, 
                                  colour = my_axis_color),
        legend.position = "bottom"
        ,legend.title=element_blank()
        ,legend.text = element_text(size = my_legend_size, 
                                    face = "bold"),
        )+
  geom_text(aes(label=..count..),
            stat = 'count',
            position = position_stack(vjust = 0.5))

ggsave("causes2.pdf")



################ plot stage_pie ##########################
# myLabels=c("back","front","middle")

#stage_palette <- c("#B8E186","#7FBC41","#4D9221") #green !!!!
stage_palette <- c("#DEEBF7","#9ECAE1","#3182BD") #blue !!!



pie_function <- function(input_data, title_){
  temp <- subset(input_data, !is.na(input_data$stages))
  total_ <- sum(table(temp$stages)) # bug number in each stage
  pie1 <- ggplot(temp, aes(x=1 ,fill=stages))
  pie1 <- pie1 + geom_bar() + 
    coord_polar(theta = "y")+
    scale_fill_manual(values = stage_palette,
                      breaks = c("Model Loading","High-Level IR Transformation","Low-Level IR Transformation"),
                      )+
    labs(title=title_)+
    theme_void() +
    theme(axis.text=element_blank(),
          axis.ticks=element_blank(),
          plot.title = element_text(hjust = 0.5, 
                                    vjust = -60, 
                                    face = "bold",
                                    size = my_title_size,
                                    colour = my_axis_color),
          legend.title=element_blank(),
          legend.text = element_text(size = my_legend_size, face = "bold"),
          legend.position = "right") +  
          # guides(fill=FALSE)+
    geom_text(aes(label=paste(round(..count.. / total_,4)*100,"%", sep = ''),x=1.1), 
              stat = 'count', size=4.8, position = position_stack(vjust =0.5 ))
  
}

pie1 <- pie_function(tvm_bugs,"TVM")
pie2 <- pie_function(glow_bugs, "Glow")
pie3 <- pie_function(ngraph_bugs, "nGraph")
#pie4 <- pie_function(bugs,"Totals",5)

#p <- pie1 +pie2 +pie3 +pie4 +plot_layout(ncol=4, guides = 'collect')
p <- pie1 +pie2 +pie3 +plot_layout(ncol=3, guides = 'collect')
p
ggsave("stage2.pdf", height=4)




