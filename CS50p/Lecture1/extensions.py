# Build the main function
def main():
    # Put the necessary extensions in a tuple
    ext = (".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")
    # Group those into MIME types
    mime = ("image/gif", "image/jpeg", "image/png", "application/pdf", "text/plain", "application/zip")
    # Get the user's file
    file = input("Filename: ").lower().strip()

    # Check which MIME type the file is and return the value
    if file.endswith(ext):
        if file.split('.')[-1] == ext[1].split('.')[-1] or file.split('.')[-1] == ext[2].split('.')[-1]:
            return print(mime[1])
        elif file.split('.')[-1] == ext[0].split('.')[-1]:
            return print(mime[0])
        elif file.split('.')[-1] == ext[3].split('.')[-1]:
            return print(mime[2])
        elif file.split('.')[-1] == ext[4].split('.')[-1]:
            return print(mime[3])
        elif file.split('.')[-1] == ext[-2].split('.')[-1]:
            return print(mime[-2])
        else:
            return print(mime[-1])
    else:
        return print("application/octet-stream")




main()