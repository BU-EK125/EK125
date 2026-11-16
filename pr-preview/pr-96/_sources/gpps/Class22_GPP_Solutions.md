# Class 22 GPP Solutions: Explore Data with MATLAB Plots

Answers to the tutorial's tasks, for the sections assigned in the
[GPP](Class22_GPP.md). The tutorial's own data-loading code (`load
gasprices`, etc.) is shown once per section since it's provided for you
by the tutorial itself.

## Types of MATLAB Plots

Setup: `load gasprices`, `Aus_Can = Australia - Canada;`

**Task 1:**
```matlab
plot(Year,Aus_Can)
```

**Task 2:**
```matlab
area(Year,Aus_Can)
```

**Task 3:**
```matlab
stem(Year,Aus_Can)
% stairs(Year,Aus_Can)  % alternate solution
% bar(Year,Aus_Can)     % alternate solution
```

## Set Plot Properties

Setup: `load gasprices`

**Task 1:**
```matlab
plot(Year,Australia,"-ok")
```

**Task 2:**
```matlab
plot(Year,Australia,"-ok",MarkerFaceColor="k")
```

**Task 3:**
```matlab
plot(Year,Canada,"--sk",MarkerFaceColor="c", MarkerSize=10, MarkerEdgeColor="r")
```

## Specify Colors

Setup: `load gasprices`, `Aus_Can = Australia-Canada;`, `plot(Year,Aus_Can)`

**Task 1:**
```matlab
plot(Year,Aus_Can,"m")
```

**Task 2:**
```matlab
plot(Year,Aus_Can,'-o',Color=[0.5 0.6 0])
```

**Task 3:**
```matlab
plot(Year,Aus_Can,'-o',Color=[0.6 0.2 0.8], MarkerFaceColor='c')
```

## Scatter Plots of Hurricane Data

Setup: `load oneHurrData`

**Task 1:**
```matlab
scatter(ws,pr,100,'r','filled')
```
