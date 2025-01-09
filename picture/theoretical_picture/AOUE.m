% Create a new figure window
figure;
% Plot the first graph
subplot(2,2, 1,'position',[0.24,0.62,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
beta = 0.01;
d = 16;
alpha_range = linspace(beta, 0.5, 100000);  % Increase the number of sampling points
n = 1000;

% Original OUE protocol adjustment
p_1 = 1/2;
q_1 = 1 / (exp(epsilon) + 1);
var_before = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + ((1 - p_1 - q_1)) / (d * n * (p_1 - q_1));

% Adjusted OUE protocol
var_after = zeros(size(alpha_range));
for i = 1:length(alpha_range)
    alpha = alpha_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2 = 1;
        q_2 = 0;
    else
        % Condition: alpha / beta > e^epsilon
        p_2 = 1 / 2;
        q_2 = (alpha - beta * exp(epsilon)) / ((exp(epsilon) - 1) + 2 * (alpha - beta * exp(epsilon)));
    end
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end

% Define marker shapes
marker_shapes = {'o', 's'};

% Plotting
plot(alpha_range, var_before * ones(size(alpha_range)), 'LineWidth', 2,'Color', [0.6235, 0, 0], 'MarkerSize', 12,'Marker', marker_shapes{1}, 'MarkerIndices', 1:10000:numel(alpha_range));
hold on;
plot(alpha_range, var_after, 'LineWidth', 2, 'Marker', marker_shapes{2},'Color', [0.0, 0.227, 0.459],'MarkerSize', 12, 'MarkerIndices', 1:10000:numel(alpha_range));
set(gca, 'FontName', 'Times New Roman');
xlabel('Conditional Probability \alpha');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('OUE', 'AOUE', 'FontName', 'Times New Roman','FontSize', 14);

% Set axis limits
xlim([beta, 0.5]);
ylim([-0.0001, 0.004]);

% Add grid lines
grid on;
% Show the plot
title('(a) \alpha', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman','position',[0.25,-0.0016,0]);
hold off;
% Plot the second graph
subplot(2, 2, 2,'position',[0.57,0.62,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
alpha = 0.1;
d = 16;
beta_range = linspace(0.000001, alpha, 50);
n = 1000;

% Original OUE protocol adjustment
p_1 = 1/2;
q_1 = 1 / (exp(epsilon) + 1);
var_before = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + ((1 - p_1 - q_1)) / (d * n * (p_1 - q_1));

% Adjusted OUE protocol
var_after = zeros(size(beta_range));
for i = 1:length(beta_range)
    beta = beta_range(i);
    if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2 = 1;
        q_2 = 0;
    else
        % Condition: alpha / beta > e^epsilon
        p_2 = 1 / 2;
        q_2 = (alpha - beta * exp(epsilon)) / ((exp(epsilon) - 1) + 2 * (alpha - beta * exp(epsilon)));
    end
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end
% Define marker shapes
marker_shapes = { 'o', 's'};
% Plotting
plot(beta_range, var_before * ones(size(beta_range)),  'Marker', marker_shapes{1}, 'Color', [0.6235, 0, 0],'MarkerSize', 12,  'MarkerIndices', 1:10:numel(beta_range),'LineWidth', 2);
hold on;
plot(beta_range, var_after,  'Marker', marker_shapes{2}, 'MarkerSize', 12, 'Color', [0.0, 0.227, 0.459], 'MarkerIndices', 1:10:numel(beta_range),'LineWidth', 2);
set(gca, 'FontName', 'Times New Roman');
xticks(0:0.02:0.1);
xlabel('Conditional Probability \beta');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('OUE', 'AOUE', 'FontName', 'Times New Roman','FontSize', 14);

% Set axis limits
xlim([0, alpha]);
ylim([0, 0.004]);

% Add grid lines
grid on;
% Show the plot
hold off;
title('(b) \beta', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman','position',[0.05,-0.00145,0]);

% Plot the third graph
subplot(2, 2, 3,'position',[0.24,0.15,0.236220472440945,0.332753710261639]);
% Parameter settings
alpha = 0.1;
beta = 0.01;
d = 16;
n = 1000;
epsilon_range = linspace(0.1, 3, 1000); % Range of values for epsilon

% Initialize error arrays
var_before = zeros(size(epsilon_range));
var_after = zeros(size(epsilon_range));
p_1 = 1/2;
% Calculate the error for original and adjusted OUE protocols
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    
    % Perturbation probabilities for the original protocol
    
    q_1 = 1 / (exp(epsilon) + 1);
    
    % Error calculation for the original protocol
    var_before(i) = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + ((1 - p_1 - q_1)) / (d * n * (p_1 - q_1));
    
    % Perturbation probabilities for the adjusted protocol
    if alpha / beta <= exp(epsilon)
        p_2 = 1;
        q_2 = 0;
    else
        p_2 = 1 / 2;
        q_2 = (alpha - beta * exp(epsilon)) / ((exp(epsilon) - 1) + 2 * (alpha - beta * exp(epsilon)));
    end
    
    % Error calculation for the adjusted protocol
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end

% Define marker shapes
marker_shapes = {'o', 's'};

% Plot curves

plot(epsilon_range, var_before, 'LineWidth', 2, 'Marker', marker_shapes{1},'Color', [0.6235, 0, 0],'MarkerSize',12,'MarkerIndices', 1:100:numel(epsilon_range));
hold on;
plot(epsilon_range, var_after, 'LineWidth', 2, 'Marker', marker_shapes{2}, 'Color', [0.0, 0.227, 0.459],'MarkerSize',12,'MarkerIndices', 1:100:numel(epsilon_range));

% Add legend and labels
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget \epsilon');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('OUE', 'AOUE', 'FontName', 'Times New Roman','FontSize', 14);

% Set axis limits
xlim([0.1, 3]);
ylim([0, 0.45]); % Automatically adjust y-axis range to fit data

% Add grid lines
grid on;
% Show the plot
title('(c) \epsilon', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman','position',[1.5,-0.16,0]);
hold off;

% Plot the fourth graph
subplot(2, 2, 4,'position',[0.57,0.15,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
alpha = 0.1;
beta = 0.01;
d_range =16:1:1024; % Range of attribute domain size d
n = 1000; % Number of users

% Initialize error arrays
var_before = zeros(size(d_range));
var_after = zeros(size(d_range));

% Perturbation probabilities for the original protocol
p_1 = 1/2;
q_1 = 1 / (exp(epsilon) + 1);
if alpha / beta <= exp(epsilon)
        % Condition: alpha / beta <= e^epsilon
        p_2 = 1;
        q_2 = 0;
    else
        % Condition: alpha / beta > e^epsilon
        p_2 = 1 / 2;
        q_2 = (alpha - beta * exp(epsilon)) / ((exp(epsilon) - 1) + 2 * (alpha - beta * exp(epsilon)));
    end
% Calculate the error for the original protocol
for i = 1:length(d_range)
    d = d_range(i);
    var_before(i) = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2) + ((1 - p_1 - q_1)) / (d * n * (p_1 - q_1));
end

% Calculate the error for the adjusted protocol
for i = 1:length(d_range)
    d = d_range(i);
    % Error calculation for the adjusted protocol
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2) + ((1 - p_2 - q_2)) / (d * n * (p_2 - q_2));
end
% Define marker shapes
marker_shapes = { 'o', 's'};
% Plot curves
plot(d_range, var_before,'Marker', marker_shapes{1}, 'MarkerSize', 12,'Color', [0.6235, 0, 0], 'MarkerIndices', 1:100:numel(epsilon_range),'LineWidth', 2);
hold on;
plot(d_range, var_after, 'Marker', marker_shapes{2}, 'MarkerSize', 12, 'Color', [0.0, 0.227, 0.459],'MarkerIndices', 1:100:numel(epsilon_range),'LineWidth', 2);

% Add legend and labels
set(gca, 'FontName', 'Times New Roman');
xlabel('Attribute Domain Size d');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('OUE', 'AOUE', 'FontName', 'Times New Roman','FontSize', 14);

% Set axis limits
xlim([16, 1024]);
ylim([0, max([var_before, var_after]) * 1.1]); % Automatically adjust y-axis range to fit data
% Add grid lines
grid on;
title('(d) d', 'HorizontalAlignment', 'center','FontWeight', 'bold', 'FontSize', 18, 'FontName', 'Times New Roman','position',[500,-0.0015,0]);
% Show the plot
hold off;
