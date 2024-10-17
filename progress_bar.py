from alive_progress import alive_bar
import  time


tasks = [1,2,3,4]
with alive_bar(len(tasks),title='processing')as bar:
    for task in tasks:
      time.sleep(0.5)
      bar.text = f'Working on {task}'
      bar()
