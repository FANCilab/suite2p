
clear;
addpath(genpath('D:\OneDrive - Fondazione Istituto Italiano Tecnologia\Documents\Code\FedBox'));
addpath('D:\OneDrive - Fondazione Istituto Italiano Tecnologia\Documents\Code\FedBox\rastermap_matlab');

%% load the data

load('Z:\Data\suite2p_tutorial\Data\2P_invivo\FR140\20190529\test\suite2p\plane0\Fall.mat')

%% PLot neuropil corrected fluorescent traces

neurons_raw = F(logical(iscell(:,1)), :);

[nN, nFrames] = size(neurons_raw);

frameTime = (1:nFrames)/ops.fs;

%% de-bleach if needed (modify to do after neuropil correction)

[neurons_deBleached, indunits] = s2pUtils.deBleach(neurons_raw', frameTime);

figure; plot(frameTime, neurons_deBleached(:, 100)); hold on;

%% subtract neuropil

neuropil = Fneu(logical(iscell(:,1)), :);

neurons = s2pUtils.estimateNeuropil_LFR(neurons_raw, neuropil);

[nN, nFrames] = size(neurons);

neurons = zscore(neurons, [], 2);

toPlot = 1:10:nN

figure;
PlotDisplacedLFR(frameTime,neurons(toPlot, :)', 3);

figure; 
imagesc(frameTime, 1:nN, neurons)


%% plot the ROIs

mimgG = ops.meanImg;

if exist('mimgR')
mimgR = ops.meanImg_chan2;
else
    mimgR = mimgG;
end

Ly = 512;%ops.Lyc;

Lx = 512;%ops.Lxc;

map = zeros(Ly, Lx);

goodROI = find([iscell(:,1)]);

nROI = numel(goodROI);

varR = zeros(size(map));

h = randperm(nROI);
for ir = 1:nROI
    ipix = sub2ind([Ly, Lx], stat{goodROI(ir)}.ypix, stat{goodROI(ir)}.xpix);
    map(ipix) = h(ir);
    vM = stat{goodROI(ir)}.lam;
    vM = vM/sum(vM.^2)^.5;
    varR(ipix) = vM;
    
end

color_opt = 1

if color_opt
%    V = max(0, min(.5 * reshape(varR, Ly, Lx)/mean(varR(:)), 2));
V = max(0, min(.2 * reshape(varR, Ly, Lx)/mean(varR(:)), 2));
H = (map-1)/max(map(:));
Sat = ones(size(V));
rgb_image= hsv2rgb(cat(3, H, Sat, V));
rgb_image(:,:,1) = 0;
else
rr = max(0, min(.5 * reshape(varRRed, Ly, Lx)/mean(varR(:)), 2));

R = 1-max(0, min(.15 * reshape(varR, Ly, Lx)/mean(varR(:)), 2));
G = 1-max(0, min(.15 * reshape(varR, Ly, Lx)/mean(varR(:)), 2));
B = 1-max(0, min(.15 * reshape(varR, Ly, Lx)/mean(varR(:)), 2));

R(rr>0) = rr(rr>0);
% R(rr>0) = c;
G(rr>0) = 0;
B(rr>0) = 0;
% R = zeros(size(R));
rgb_image = cat(3, R,G,B);
end

figure;
g = subplot(1,3,1);
imagesc(mat2gray(mimgG)); axis image;
set(gca, 'XTick', [], 'XTickLabel', [], 'YTick', [], 'YTickLabel', [])
caxis([0.05 0.3]); colormap(g, 'gray');

r = subplot(1,3,2);
imagesc(mat2gray(mimgR)); axis image;
set(gca, 'XTick', [], 'XTickLabel', [], 'YTick', [], 'YTickLabel', [])
caxis([0.05 0.3]); colormap(r, Reds(100));

ror = subplot(1,3,3);
ro = imagesc(rgb_image); axis image;
set(gca, 'XTick', [], 'XTickLabel', [], 'YTick', [], 'YTickLabel', [])
set(ro, 'alphadata', map ~= 0)
formatAxes

%% raster map

[nN, nT] = size(neurons);

[iclustup, isort, Vout] = activityMap(neurons);

neurons_sorted = neurons(isort,:);

figure('Color', 'White');
imagesc(frameTime, 1:nN, neurons_sorted ); hold on
xlabel('Time(s)');
ylabel('Neurons (zscore)');


%% try to understand when stims happened

% stimulation started at 6.7 seconds. 

meanN = gaussFilt(mean(neurons,1)', 10);
Dmean = [0; diff(meanN)];

figure; 

plot(frameTime ,meanN)


