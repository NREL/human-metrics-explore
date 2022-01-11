###packages
library(readxl)
library(data.table)
library(dplyr)
library(rlist)

###no of iterations
n <- 10000

###assign values

####speed
l_speed_walkbike <- 5
u_speed_walkbike <- 20

l_speed_car <- 25
u_speed_car <- 100

l_speed_bus <- 15
u_speed_bus <- 30

####avo
avo_walkbike <- 1

l_avo_car <- 1 ###this is just min max , not values from the distribution of sample means
u_avo_car <- 7


l_avo_bus <- 6.075
u_avo_bus <- 14.675

###pmt
l_pmt_walkbike <- 0.2055
u_pmt_walkbike <- 7.7204

l_pmt_car <- 4.362
u_pmt_car <- 16.387

l_pmt_bus <- 0.086
u_pmt_bus <- 88.356

###ms
l_ms_walkbike <- 0.06
u_ms_walkbike <- 0.36

l_ms_car <- 0.61
u_ms_car <- 0.93

l_ms_bus <- 0
u_ms_bus <- 0.12

###length of mode + total length

l_lm_walkbike <- 1
u_lm_walkbike <- 2


l_lm_car <- 4
u_lm_car <- 6


l_lm_bus <- 10
u_lm_bus <- 20

###modes per width
mpw_walkbike <- 2

mpw_car <- 1

mpw_bus <- 1

###generate vectors of random nos
speed_walkbike <- round(runif(n,l_speed_walkbike,u_speed_walkbike),4)
speed_car <- round(runif(n,l_speed_car,u_speed_car),4)
speed_bus <- round(runif(n,l_speed_bus,u_speed_bus),4)

avo_car <- round(runif(n,l_avo_car,u_avo_car),4)
avo_bus <- round(runif(n,l_avo_bus,u_avo_bus),4)

pmt_walkbike <- round(runif(n,l_pmt_walkbike,u_pmt_walkbike),4)
pmt_car <- round(runif(n,l_pmt_car,u_pmt_car),4)
pmt_bus <- round(runif(n,l_pmt_bus,u_pmt_bus),4)

ms_walkbike <- round(runif(n,l_ms_walkbike,u_ms_walkbike),4)
ms_car <- round(runif(n,l_ms_car,u_ms_car),4)
ms_bus <- round(runif(n,l_ms_bus,u_ms_bus),4)

twosec_dist_walkbike <- speed_walkbike * 1000/3600 *2
twosec_dist_car <- speed_car * 1000/3600 *2
twosec_dist_bus <- speed_bus * 1000/3600 *2

lm_walkbike <- round(runif(n,l_lm_walkbike,u_lm_walkbike),4)
lm_car <- round(runif(n,l_lm_car,u_lm_car),4)
lm_bus <- round(runif(n,l_lm_bus,u_lm_bus),4)

tl_walkbike <- twosec_dist_walkbike + lm_walkbike
tl_car <- twosec_dist_car + lm_car
tl_bus <- twosec_dist_bus + lm_bus

###create empty vectors
vphpl_combined_vec <- c()
pphpl_combined_vec <- c()
pphpl_1_combined_vec <- c()

###derived vectors
vphpl_walkbike <- 0
vphpl_car <- speed_car*1000/tl_car
vphpl_bus <- speed_bus*1000/tl_bus

pphpl_walkbike <- speed_walkbike*1000/tl_walkbike * mpw_walkbike * avo_walkbike * (10/(pmt_walkbike*1.6))
pphpl_car <- speed_car*1000/tl_car * mpw_car * avo_car * (10/(pmt_car*1.6))
pphpl_bus <- speed_bus*1000/tl_bus * mpw_bus * avo_bus * (10/(pmt_bus*1.6))

pphpl_1_walkbike <- speed_walkbike*1000/tl_walkbike * mpw_walkbike * avo_walkbike
pphpl_1_car <- speed_car*1000/tl_car * mpw_car * avo_car 
pphpl_1_bus <- speed_bus*1000/tl_bus * mpw_bus * avo_bus

vphpl_combined_vec <- ms_walkbike*vphpl_walkbike + ms_car*vphpl_car + ms_bus*vphpl_bus
pphpl_combined_vec <- ms_walkbike*pphpl_walkbike + ms_car*pphpl_car + ms_bus*pphpl_bus
pphpl_1_combined_vec <- ms_walkbike*pphpl_1_walkbike + ms_car*pphpl_1_car + ms_bus*pphpl_1_bus

#for (i in 1:100)
#{

###VPHPL
#vphpl_combined_vec[i] <- ms_walkbike[i]*vphpl_walkbike + ms_car[i]*vphpl_car[i] + ms_bus[i]*vphpl_bus[i]

#vphpl_combined_vec <- vphpl_combined_vec %>% append(vphpl_combined)

###PPHPL (10km)
#pphpl_combined_vec[i] <- ms_walkbike[i]*pphpl_walkbike[i] + ms_car[i]*pphpl_car[i] + ms_bus[i]*pphpl_bus[i]

#pphpl_combined_vec <- pphpl_combined_vec %>% append(pphpl_combined)

###PPHPL (no pmt)
#pphpl_1_combined_vec[i] <- ms_walkbike[i]*pphpl_1_walkbike[i] + ms_car[i]*pphpl_1_car[i] + ms_bus[i]*pphpl_1_bus[i]

#pphpl_1_combined_vec <- pphpl_1_combined_vec %>% append(pphpl_1_combined)
#}

###visualizations
par(mfrow = c(3,1))

hist(vphpl_combined_vec, c=("green"),breaks = 100)
print(summary(vphpl_combined_vec))
print(sd(vphpl_combined_vec))

hist(pphpl_combined_vec, c=("green"),breaks = 100)
print(summary(pphpl_combined_vec))
print(sd(pphpl_combined_vec))

hist(pphpl_1_combined_vec, c=("green"),breaks = 100)
print(summary(pphpl_1_combined_vec))
print(sd(pphpl_1_combined_vec, na.rm = TRUE))

