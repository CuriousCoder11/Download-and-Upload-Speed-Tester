while True:
  import speedtest

  st = speedtest.Speedtest()

  option = int(input('''What speed do you want to test:

    1) Download Speed   
    
    2) Upload Speed

    3) Both
    
    1, 2 or 3: '''))

  print("This will take a few seconds...\n")

  if option == 1:
      print("Download Speed: ",st.download(),"mb/s\n")

  elif option == 2:
      print("Upload Speed: ",st.upload(),"mb/s\n")

  elif option == 3:
    print("Download Speed: ",st.download(),"mb/s")
    print("Upload Speed: ",st.upload(),"mb/s\n")

  else:
      print("Please enter the correct choice!")

  test_again = int(input('''Do you want to run the test again?:

    1) Yes

    2) No
  
  1 or 2: '''))
  if test_again == 1:
      continue

  elif test_again == 2:
      print("We're so glad that you tested your network speed withour service!")
      break