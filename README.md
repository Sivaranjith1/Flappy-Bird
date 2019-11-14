# Genetic algorithm learn to play Flappy Bird
It was first a flappy bird game created in pygame. Afterwards a neutral network where added on top to make an ai play the game by itself.

## Packages
```txt
Markdown==3.1.1
numpy==1.16.4
numpydoc==0.9.1
py==1.8.0
pycodestyle==2.5.0
pygame==1.9.6
Pygments==2.4.2
pylint==2.4.3
pywin32==223
scipy==1.2.1

```

## Fitness score
![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B100*%7CnextPipe_%7Bcenter%7D%20-%20bird_%7By_%7Bpos%7D%7D%7C%7D%20&plus;%20score)

And a if statement ensure that the fraction won't exceed 0.6