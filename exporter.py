import os
import shutil
import json
import argparse

def copy_manifest_and_blobs(models_dir, model_name, tag_name, target_path):
    # Define paths
    manifest_path = os.path.join(models_dir, 'manifests', 'registry.ollama.ai', 'library', model_name, tag_name)
    blobs_dir = os.path.join(models_dir, 'blobs')
    
    # Check if manifest file exists
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest file not found: {manifest_path}")
    
    # Load the manifest file
    with open(manifest_path, 'r') as manifest_file:
        manifest = json.load(manifest_file)
    
    # Create target directories
    target_manifests_dir = os.path.join(target_path, 'manifests', 'registry.ollama.ai', 'library', model_name)
    target_blobs_dir = os.path.join(target_path, 'blobs')
    
    os.makedirs(target_manifests_dir, exist_ok=True)
    os.makedirs(target_blobs_dir, exist_ok=True)
    
    # Copy manifest file
    shutil.copy2(manifest_path, os.path.join(target_manifests_dir, tag_name))
    
    # Copy blob files
    for layer in manifest['layers']:
        digest = layer['digest'].replace(':', '-')
        blob_path = os.path.join(blobs_dir, digest)
        if not os.path.exists(blob_path):
            raise FileNotFoundError(f"Blob file not found: {blob_path}")
        shutil.copy2(blob_path, os.path.join(target_blobs_dir, digest))

def main():
    parser = argparse.ArgumentParser(description="Export Ollama model manifest and blobs to a new location.")
    parser.add_argument('model_name', type=str, help="Name of the model.")
    parser.add_argument('tag_name', type=str, help="Tag name of the model.")
    parser.add_argument('target_path', type=str, help="Target path to export the files.")
    parser.add_argument('--models_dir', type=str, default=os.path.expanduser('~/.ollama/models'), help="Directory where the models are stored. Default is ~/.ollama/models.")
    
    args = parser.parse_args()
    
    try:
        copy_manifest_and_blobs(args.models_dir, args.model_name, args.tag_name, args.target_path)
        print(f"Successfully exported {args.model_name}:{args.tag_name} to {args.target_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()