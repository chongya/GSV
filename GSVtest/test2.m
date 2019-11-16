% This script shows how to simulate different soil spectra by changing coefficients

wvl = 400:10:2500;
DryVec = importdata('MD.vec.txt');
SMVec = importdata('SM.vec.txt');
V = [DryVec;SMVec];
for c1 = [0.3,0.7]
    for c2 = [-0.1,0]
        for c3 = [0,0.05]
            for cSM = [-0.2,0]
                spec = c1*V(1,:) + c2*V(2,:) + c3*V(3,:) + cSM*V(4,:);
                plot(wvl,spec);xlim([400,2500]);ylim([0,1]);hold on;
            end
        end
    end
end
