% Create a new figure window
figure;
d=10;
% Plot the first graph
subplot(1,3, 1,'position',[0.085,0.35,0.236220472440945,0.332753710261639]);
% Set parameters
epsilon = 1;
beta_values = [0.01, 0.05, 0.1];

% Define marker shapes
marker_shapes = {'^', 'o', 's', 'x'};
marker_size = 12; % Increase marker size
% Set axis range
xlim([0, 0.2]);
ylim([0.5, 1.1]);
set(gca, 'FontName','Times New Roman','FontSize', 16); % Set axis font size
line_color1 = [0.0, 0.227, 0.459]; % Blue
line_color2 = [0.6235, 0, 0]; % Orange
line_color3 = [0.9290, 0.6940, 0.1250]; % Yellow


% Plot curves
beta = beta_values(1);
alpha_range = linspace(beta, 0.2, 100);

p_2 = zeros(size(alpha_range));
for i = 1:length(alpha_range)
    alpha = alpha_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end

plot(alpha_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{1}, 'Color',[0.0, 0.227, 0.459],'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(alpha_range));
hold on;
beta = beta_values(2);
alpha_range = linspace(beta, 0.2, 100);
p_2 = zeros(size(alpha_range));
for i = 1:length(alpha_range)
    alpha = alpha_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end
plot(alpha_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{2}, 'Color',[0.6235, 0, 0],'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(alpha_range));
hold on;
beta = beta_values(3);
alpha_range = linspace(beta, 0.2, 100);
p_2 = zeros(size(alpha_range));
for i = 1:length(alpha_range)
    alpha = alpha_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end
plot(alpha_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{3}, 'Color',[0.9290, 0.6940, 0.1250],'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(alpha_range));

% Plot p_2 = 1 line
x_range = linspace(0, 0.2, 100);
y_p1_1 = ones(size(x_range));
plot(x_range, y_p1_1, 'LineWidth', 1.5, 'Marker', marker_shapes{end}, 'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(x_range), 'Color', [0.4940, 0.1840, 0.5560]); % Use new marker shape and color
% Plot vertical dashed lines
for i = 1:numel(beta_values)
    alpha = beta_values(i);
    x_line = alpha * ones(size(ylim));
    % Select corresponding color based on index
    switch i
        case 1
            line_color = [0.0, 0.227, 0.459]; % Blue
        case 2
            line_color = [0.6235, 0, 0]; % Orange
        case 3
            line_color = [0.9290, 0.6940, 0.1250]; % Yellow
    end
    
    line(x_line, [0.5,1], 'LineStyle', '--', 'Color', line_color,'LineWidth', 1);
end

% Label x-axis
text(0.008, 0.47, '0.01', 'FontName', 'Times New Roman', 'Color', [0, 0.4470, 0.7410], 'FontSize', 12);

% Set axis labels and title
xlabel('Conditional Probability \alpha', 'FontName', 'Times New Roman', 'FontSize', 16);
ylabel('p_2', 'FontName', 'Times New Roman', 'FontSize', 16);
legend('\beta = 0.01', '\beta = 0.05', '\beta = 0.1', '\beta = \alpha/e^\epsilon', 'FontName', 'Times New Roman', 'FontSize', 14,'Location','southwest');
% Add grid lines
grid on;

% Set axis border
box on;
title('(a) \alpha', 'FontName', 'Times New Roman', 'FontSize', 18, 'FontWeight', 'bold','position',[0.1,0.27,0]);


% Plot the second graph
subplot(1, 3, 2,'position',[0.395,0.35,0.236220472440945,0.332753710261639]);
% Set parameters
epsilon = 1;
alpha_values = [0.2, 0.15, 0.1];
hold on;
% Define marker shapes
marker_shapes = {'^', 'o', 's', 'x'};
marker_size = 12; % Increase marker size
% Plot curves

alpha = alpha_values(1);
beta_range = linspace(0, alpha, 100);
p_2 = zeros(size(beta_range));
for i = 1:length(beta_range)
    beta = beta_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end

plot(beta_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{1}, 'Color',[0.0, 0.227, 0.459],'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(beta_range)); % Use different color, increase line width
hold on;
alpha = alpha_values(2);
beta_range = linspace(0, alpha, 100);
p_2 = zeros(size(beta_range));
for i = 1:length(beta_range)
    beta = beta_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end

plot(beta_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{2},'Color',[0.6235, 0, 0], 'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(beta_range)); % Use different color, increase line width
hold on;
alpha = alpha_values(3);
beta_range = linspace(0, alpha, 100);
p_2 = zeros(size(beta_range));
for i = 1:length(beta_range)
    beta = beta_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end

plot(beta_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{3}, 'Color',[0.9290, 0.6940, 0.1250],'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(beta_range)); % Use different color, increase line width

% Plot p_1 = 1 line
x_range = linspace(0, max(alpha_values), 100);
y_p1_1 = ones(size(x_range));
plot(x_range, y_p1_1, 'LineWidth', 1.5, 'Marker', marker_shapes{end}, 'MarkerSize', marker_size, 'MarkerIndices', 1:20:numel(x_range), 'Color', [0.4940, 0.1840, 0.5560]); 

% Plot vertical dashed lines
for i = 1:numel(alpha_values)
alpha = alpha_values(i);
x_line = alpha * ones(size(ylim));% Select corresponding color based on index
switch i
    	case 1
            line_color = [0.0, 0.227, 0.459]; % Blue
        case 2
            line_color = [0.6235, 0, 0]; % Orange
        case 3
            line_color = [0.9290, 0.6940, 0.1250]; % Yellow
end

line(x_line, ylim, 'LineStyle', '--', 'Color', line_color, 'LineWidth', 1); % Increase line width
end
% Set axis labels and title
xlabel('Conditional Probability \beta', 'FontName', 'Times New Roman', 'FontSize', 16); % Increase font size
ylabel('p_2', 'FontName', 'Times New Roman', 'FontSize', 16); % Increase font size
legend('\alpha = 0.2', '\alpha = 0.15', '\alpha = 0.1', '\alpha = \betae^\epsilon', 'FontName', 'Times New Roman', 'FontSize', 14, 'Location','southeast'); % Increase font size, adjust legend position

% Set axis range
xlim([0, max(alpha_values)]);
ylim([0.4, 1.1]);
set(gca, 'FontSize', 16, 'FontName', 'Times New Roman'); % Set axis font size
% Add grid lines
grid on;
% Set axis border
box on;

hold off;

title('(b) \beta', 'FontName', 'Times New Roman', 'FontSize', 18, 'FontWeight', 'bold','position',[0.1,0.12,0]);


% Plot the third graph
subplot(1,3, 3,'position',[0.7,0.35,0.236220472440945,0.332753710261639]);
% Set parameters
alpha = 0.1;
beta_values = [0.01, 0.05, 0.1];

hold on;

% Define marker shapes
marker_shapes = {'^', 'o', 's', 'x'};

% Plot curves

beta = beta_values(1);
epsilon_range = linspace(0.1, 3, 100);
p_2 = zeros(size(epsilon_range));
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end

plot(epsilon_range, p_2, 'LineWidth', 2 ,'Marker', marker_shapes{1},  'Color',[0.0, 0.227, 0.459],'MarkerSize', 12,'MarkerIndices', 1:20:numel(epsilon_range));
hold on;
beta = beta_values(2);
p_2 = zeros(size(epsilon_range));
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end
plot(epsilon_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{2},  'Color',[0.6235, 0, 0],'MarkerSize', 12,'MarkerIndices', 1:20:numel(epsilon_range));
hold on;
beta = beta_values(3);
p_2 = zeros(size(epsilon_range));
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2(i) = 1;
    else
        p_2(i) = ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - (d + 1) * alpha) - (1 - (d + 1) * beta) * exp(epsilon));
    end
end

plot(epsilon_range, p_2, 'LineWidth', 2, 'Marker', marker_shapes{3},  'Color',[0.9290, 0.6940, 0.1250],'MarkerSize', 12,'MarkerIndices', 1:20:numel(epsilon_range));
hold on;

% Plot p_1 = 1 line
x_range = linspace(0.1, 3, 100);
y_p1_1 = ones(size(x_range));
plot(x_range, y_p1_1, 'LineWidth', 1.5, 'Marker', marker_shapes{end}, 'MarkerSize', 12,'MarkerIndices', 1:20:numel(x_range), 'Color', [0.4940, 0.1840, 0.5560]); % Use new marker shape and color

% Add vertical line
line([0.1, 0.1],[0,1], 'LineStyle', '--', 'Color', [0.6350, 0.0780, 0.1840], 'LineWidth', 1); % Red dashed line
% Set axis range
xlim([0, 3]);
ylim([0.1, 1.1]);
set(gca, 'FontSize', 16,'FontName', 'Times New Roman'); % Set axis font size
% Get current axis limits
xlim_values = xlim;
ylim_values = ylim;

% Label x-axis
text(0.1, ylim_values(1) - 0.05 * diff(ylim_values), '0.1', 'FontName', 'Times New Roman', 'Color', [0.6350, 0.0780, 0.1840],'FontSize', 12); % Red text

% Set axis labels and title
xlabel('Privacy Budget \epsilon', 'FontName', 'Times New Roman','FontSize', 16);
ylabel('p_2', 'FontName', 'Times New Roman','FontSize', 16);
legend('\beta = 0.01', '\beta = 0.05', '\beta = 0.1', '\beta = \alpha/e^\epsilon', 'FontName', 'Times New Roman','FontSize', 14,'Location','southeast');


% Add grid lines
grid on;
box on;
title('(c) \epsilon', 'FontName', 'Times New Roman', 'FontSize', 18, 'FontWeight', 'bold','position',[1.5,-0.28,0]);
hold off;