% Create a new figure window
figure;
% Plot the first graph
subplot(1,3, 1,'position',[0.085,0.35,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
beta = 0.01;
d = 8;
alpha_range = linspace(beta, 0.5, 100);
n = 1000;

% Before adjustment RR protocol
p_1 = exp(epsilon) / (1 + exp(epsilon));
q_1 = 1 - p_1;
var_before = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2);

% After adjustment RR protocol
var_after = zeros(size(alpha_range));
for i = 1:length(alpha_range)
    alpha = alpha_range(i);
    p_2 = min(1, ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - 2 * alpha) - (1 - 2 * beta) * exp(epsilon)));
    q_2 = 1 - p_2;
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2);
end

% Define marker shapes
marker_shapes = {'o', 's', '^'};

% Plot
plot(alpha_range, var_before * ones(size(alpha_range)), 'Color', [0.6235, 0, 0],'LineWidth', 2, 'Marker', marker_shapes{1},'MarkerSize', 12, 'MarkerIndices', 1:20:numel(alpha_range));
hold on;
plot(alpha_range, var_after,'Color', [0.0, 0.227, 0.459], 'LineWidth', 2, 'Marker', marker_shapes{2},'MarkerSize', 12, 'MarkerIndices', 1:20:numel(alpha_range));
set(gca, 'FontName', 'Times New Roman');
xlabel('Conditional Probability \alpha');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('RR', 'ARR', 'FontName', 'Times New Roman','FontSize',14 );

% Set axis limits
xlim([beta, 0.5]);
ylim([0, 0.001]);

% Add grid lines
grid on;

title('(a) \alpha', 'HorizontalAlignment', 'center', 'FontSize', 18,'FontWeight', 'bold', 'FontName', 'Times New Roman','position',[0.255000402973533,-0.0004,0]);
hold off;

% Plot the second graph
subplot(1, 3, 2,'position',[0.395,0.35,0.236220472440945,0.332753710261639]);
% Parameter settings
epsilon = 1;
alpha = 0.1;
beta_range = linspace(0.000001, alpha, 10000);
n = 1000;

% Before adjustment RR protocol
p_1 = exp(epsilon) / (1 + exp(epsilon));
q_1 = 1 - p_1;
var_before = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2);

% After adjustment RR protocol
var_after = zeros(size(beta_range));
for i = 1:length(beta_range)
    beta = beta_range(i);
    p_2 = min(1, ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - 2 * alpha) - (1 - 2 * beta) * exp(epsilon)));
    q_2 = 1 - p_2;
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2);
end

% Define marker shapes
marker_shapes = { 'o', 's'};

% Plot
plot(beta_range, var_before * ones(size(beta_range)),  'Color', [0.6235, 0, 0],'LineWidth', 2, 'Marker', marker_shapes{1}, 'MarkerSize', 12, 'MarkerIndices', 1:2000:numel(beta_range));
hold on;
plot(beta_range, var_after, 'Color', [0.0, 0.227, 0.459],'LineWidth', 2, 'Marker', marker_shapes{2}, 'MarkerSize', 12, 'MarkerIndices', 1:2000:numel(beta_range));
set(gca, 'FontName', 'Times New Roman');
xticks(0:0.02:0.1);
xlabel('Conditional Probability \beta');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('RR', 'ARR', 'FontName', 'Times New Roman','FontSize', 14);

% Set axis
xlim([0, alpha]);
ylim([0,  0.001]);
% Add grid lines
grid on;
% Show the plot
hold off;
title('(b) \beta', 'HorizontalAlignment', 'center', 'FontSize', 18,'FontWeight', 'bold', 'FontName', 'Times New Roman','position',[0.050000207952478,-0.0004,0]);

% Plot the third graph
subplot(1, 3, 3,'position',[0.715,0.35,0.236220472440945,0.332753710261639]);
% Parameter settings
alpha = 0.1;
beta = 0.01;
d = 8;
epsilon_range = linspace(0.1, 3, 100000);
n = 1000;

% Before adjustment GRR protocol
var_before = zeros(size(epsilon_range));
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    p_1 = exp(epsilon) / (1 + exp(epsilon));
    q_1 = 1 - p_1;
    var_before(i) = (q_1 * (1 - q_1)) / (n * (p_1 - q_1)^2);
end

% After adjustment GRR protocol
var_after = zeros(size(epsilon_range));
for i = 1:length(epsilon_range)
    epsilon = epsilon_range(i);
    p_2 = min(1, ((1 - alpha) - (1 - beta) * exp(epsilon)) / ((1 - 2 * alpha) - (1 - 2 * beta) * exp(epsilon)));
    q_2 = 1 - p_2;
    var_after(i) = (q_2 * (1 - q_2)) / (n * (p_2 - q_2)^2);
end

% Define marker shapes
marker_shapes = {'o', 's'};

% Plot
plot(epsilon_range, var_before, 'LineWidth', 2, 'Color', [0.6235, 0, 0],'Marker', marker_shapes{1}, 'MarkerSize', 12, 'MarkerIndices', 1:20000:numel(epsilon_range));
hold on;
plot(epsilon_range, var_after, 'LineWidth', 2, 'Color', [0.0, 0.227, 0.459],'Marker', marker_shapes{2}, 'MarkerSize', 12, 'MarkerIndices', 1:20000:numel(epsilon_range));
set(gca, 'FontName', 'Times New Roman');
xlabel('Privacy Budget \epsilon');
ylabel('Mean Squared Error');
set(gca, 'FontSize', 16);
legend('RR', 'ARR', 'FontName', 'Times New Roman','FontSize', 14);

% Set axis limits
xlim([0.1, 3]);
ylim([0,0.11]);
% Add grid lines
grid on;
% Show the plot
title('(c) \epsilon', 'HorizontalAlignment', 'center', 'FontSize', 18,'FontWeight', 'bold', 'FontName', 'Times New Roman','position',[1.554802968399831,-0.044,0]);
hold off;
