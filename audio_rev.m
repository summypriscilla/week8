inputfile='/home/rguktrkvalley/Desktop/cl/week8/sample-3s.wav'
outputfile='/home/rguktrkvalley/Desktop/cl/week8/sample-3s.wav'
[y,Fs]=audioread(inputfile);
reversedData=flipud(y);
audiowrite(outputfile,reversedData,Fs);
disp('audio is reversed and successfully saved')