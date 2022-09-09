from coalas import csvReader as c
from sklearn.metrics import accuracy_score
c.importCSV('s.csv')
c.printHeaders()


print(f'TextBlob Accuracy: {accuracy_score(c.trained,c.naiveB)}')
# Comparing Trained and Dictactions
#accuracy_score(y_true, y_pred)
#print(f'{c.col.BOLD}{c.col.CYAN}Comparing against training data{c.col.ENDC}')
#print(f'TextBlob Accuracy: {accuracy_score(c.Trained,c.TextBlobPol)}')
#print(f'Vader Accuracy: {accuracy_score(c.Trained,c.VaderPol)}')
#print(f'Dict Accuracy: {accuracy_score(c.Trained,c.DictPol)}')
#print(f'Algo Accuracy: {accuracy_score(c.Trained,c.TecAction)}')
#
#
#print(f'{c.col.BOLD}{c.col.CYAN}Comparing against Perfect{c.col.ENDC}')
#print(f'TextBlob Accuracy: {accuracy_score(c.Best,c.TextBlobPol)}')
#print(f'Vader Accuracy: {accuracy_score(c.Best,c.VaderPol)}')
#print(f'Dict Accuracy: {accuracy_score(c.Best,c.DictPol)}')
#print(f'Algo Accuracy: {accuracy_score(c.Best,c.TecAction)}')
#print(f'Trained: {accuracy_score(c.Best,c.Trained)}')
#
#
#print(f'{c.col.BOLD}{c.col.CYAN}Comparing against Worst{c.col.ENDC}')
#print(f'TextBlob Accuracy: {accuracy_score(c.Worst,c.TextBlobPol)}')
#print(f'Vader Accuracy: {accuracy_score(c.Worst,c.VaderPol)}')
#print(f'Dict Accuracy: {accuracy_score(c.Worst,c.DictPol)}')
#print(f'Algo Accuracy: {accuracy_score(c.Worst,c.TecAction)}')
#print(f'Trained Accuracy: {accuracy_score(c.Worst,c.TecAction)}')

