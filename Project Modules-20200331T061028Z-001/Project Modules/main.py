print('List of modules:\n1.Facebook post image or text\n2.Send and Email\n3.Google Search\n4.Search for a location')
choice = int(input("Enter the number of module you want to run:"))
if choice == 1:
    import facebook
elif choice == 2:
    import mail
elif choice == 3:
    import google_search
elif choice == 4:
    import google_maps