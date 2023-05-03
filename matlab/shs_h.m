% Stiahnutie programu "GrafLab" na výpočet sférického harmonického rozvoja
unzip("https://github.com/blazej-bucha/graflab/archive/refs/heads/" + ...
      "master.zip", ".");

% Zmena pracovného adresára na adresár so zdrojovým kódom programu GrafLab
cd graflab-master/src/

% Výpočet a zobrazenie zemskej topografie do rôznych stupňov "nmax"
for nmax = [30, 90, 360]

    GrafLab('OK', 1.0, 1.0, 0, nmax, [0 0 0 0 0], ...
            '../data/input/DTM2006.mat', 1, 0, -90.0, 0.25, 90, 0.0 ,0.25, ...
            360.0, 0.0, [], [], [], [], ...
            sprintf('../../../figs/shs-topography/topography-nmax%d', ...
            nmax), 0, 11, 1, [], 1, 0, 0, 2, 6, 1, 60, 600, 1);

end

% Návrat do pôvodného pracovného adresára
cd ../../
