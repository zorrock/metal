lm_model_defaults = {
    ### GENERAL
    'seed': None,
    'verbose': True,
    'show_plots': True,
    
    ### TRAIN
    'train_config': {
        # Classifier
        'cardinality': 2,
        # Class balance (if learn_class_balance=False, fix to class_balance)
        'learn_class_balance': False,
        # Class balance initialization / prior
        'class_balance': None, # TODO: (array) If None, assume uniform
        # Model params initialization / priors
        'mu_init': 0.4, 
        # L@ regularization (around prior values)
        'l2': 0.0,
        # Optimizer
        'optimizer_config': {
            'optimizer_common': {
                'lr': 0.1,
            },
            # Optimizer - SGD
            'sgd_config': {
                'momentum': 0.9, 
            },
        },
        # Train loop
        'n_epochs': 100, 
        'print_at': 10, 
    },
}
