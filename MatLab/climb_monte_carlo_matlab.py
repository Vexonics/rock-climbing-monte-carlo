import matlab.engine
import random

eng = matlab.engine.start_matlab()
results = [random.uniform(5, 30) for _ in range(50)]
mat_results = matlab.double([float(r) for r in results])

fig = eng.figure(nargout=1)
eng.plot(mat_results, '-o', 'LineWidth', 2, 'MarkerSize', 8, nargout=0)
eng.title('Monte Carlo Climbing Fatigue', nargout=0)
eng.xlabel('Trial', nargout=0)
eng.ylabel('Frequency', nargout=0)
eng.grid('on',nargout=0)
eng.drawnow(nargout=0)     
eng.uiwait(fig, nargout=0)  
