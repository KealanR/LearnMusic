from app import application

#wont be able to run on c9 without this
if __name__ == '__main__':
     application.run(host='0.0.0.0', port=8080, debug=True)