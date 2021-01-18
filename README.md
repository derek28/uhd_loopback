# uhd_loopback
USRP N210 TX-RX loopback program. UHD version 3.14. 
GPIO triggering configured for UCSD MCube. 
This program sends a single tone signal from USRP TX port, receives the signal at USRP RX port and write the data to a file. A python script is writted to read the data file and plot the power spectral density. 
