import pandas as pd
import os

def load_data(base_path='data/retailrocket/'):
    """Loads RetailRocket dataset"""
    events = pd.read_csv(os.path.join(base_path, 'events.csv'))
    item_properties1 = pd.read_csv(os.path.join(base_path, 'item_properties_part1.csv'))
    item_properties2 = pd.read_csv(os.path.join(base_path, 'item_properties_part2.csv'))
    category_tree = pd.read_csv(os.path.join(base_path, 'category_tree.csv'))
    
    return events, item_properties1, item_properties2, category_tree

def prepare_interaction_data(events):
    """Prepares user-item interaction dataframe"""
    # Only keep view and purchase events
    events = events[events['event'].isin(['view', 'purchase'])]

    # Keep necessary columns
    interactions = events[['visitorid', 'itemid', 'event', 'timestamp']]
    
    return interactions
