function signal = interpNaN(signal, method)
if nargin <2
    method = 'linear';
end

nanp = isnan(signal);
gdp = find(~nanp);
signal = signal(gdp);
signal = interp1(gdp, signal, 1:numel(nanp),method);

first_good = find(~isnan(signal), 1, 'first');
last_good = find(~isnan(signal), 1, 'last');

signal(1:first_good) = signal(first_good);
signal(last_good:end) = signal(last_good);

end