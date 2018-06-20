import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processos = ('processo1.py', 'processo2.py', 'processo3.py')                                    
                                                  
                                                                                
def roda_processo(processo):                                                             
    os.system('python {}'.format(processo))                                       
                                                                                
                                                                                
pool = Pool(processes=3)                                                        
pool.map(roda_processo, processos)