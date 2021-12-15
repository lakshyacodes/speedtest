# Python program to test
# internet speed

import speedtest


st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:

1) Download Speed

2) Upload Speed

3) Ping

Your Choice: '''))


if option == 1:

	print(f"Download Speed:{st.download()/1024/1024:.2f}MBit/s")

elif option == 2:
	print(f"Upload Speed:{st.upload()/1024/1024:.2f}MBit/s")

elif option == 3:

	servernames =[]

	st.get_servers(servernames)
	print(f"Ping:{st.results.ping:.2f}ms")
	
else:

	print("Please enter the correct choice !")
