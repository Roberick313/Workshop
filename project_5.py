#### Histogram

def my_histogram(*a):
     '''this function take a args and has a defult args in case that doesn't any...\n
     \rand it will retunr histogram of the entery args '''
     
     if a:
          pass

     else:
          a = (1,2,3,4,5,6,7,8,9,10)
     
     f =open('My_histogram.txt','w')
     f.write('')
     f.close()

     for i in a:
          c = ""
          d = 0

          while d < int(i):
               c += "*"
               d += 1

          f = open('My_histogram.txt','a')
          f.write(str(i)+' '+c+'\n')
          f.close()

     return open('My_histogram.txt').read()

