% This script shows how to reconstruct hyperspectral soil reflectance from observed multispectral soil reflectance

WVL = 400:10:2500;
DryVec = importdata('MD.vec.txt');
SMVec = importdata('SM.vec.txt');
GSV = [DryVec;SMVec];

wvl = [450,550,650,850,1650,2150];
[~,idx] = intersect(WVL,wvl,'stable');
gsv = GSV(:,idx);

hyper = csvread('TestSpectrum.csv',1,0);
multi = hyper(:,idx);

X = multi;
V = gsv;
C = X * pinv(V);

X = hyper;
V = GSV;
R = C * V;

hold on
plot(WVL,hyper,'k--')
plot(wvl,multi,'ko')
plot(WVL,R,'r-')
