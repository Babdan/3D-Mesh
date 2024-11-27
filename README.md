
# 3D-Mesh Project Documentation

This documentation outlines the current state of the 3D-Mesh project, including required libraries, CUDA-specific variations, and setup instructions for replication.

---

## **Project Overview**
The 3D-Mesh project generates 3D objects and corresponding meshes from text prompts using SHAP-E and PyTorch. The project includes lattice generation for structural designs and exports `.PLY` and `.OBJ` files for use in 3D visualization or printing.

---

## **Current State**
### **Key Features**
1. **Text-to-3D Generation**:
   - Generates 3D objects from natural language prompts.
   - Utilizes SHAP-E and NeRF-based rendering.

2. **Mesh Generation**:
   - Generates and saves meshes in `.PLY` and `.OBJ` formats.

3. **GPU Acceleration**:
   - Supports CUDA for faster processing with NVIDIA GPUs.

4. **Interactive Outputs**:
   - Visualizes 3D outputs and renders images.

---

## **Required Libraries and Versions**
### **Core Libraries**
1. **PyTorch (CUDA-enabled)**:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```
   - Installed version: `torch 2.0` with CUDA 11.8.

2. **SHAP-E**:
   - Clone and install from the repository:
     ```bash
     git clone https://github.com/openai/shap-e
     cd shap-e
     pip install -e .
     ```

3. **PyVista** (for visualization):
   ```bash
   pip install pyvista
   ```

4. **SciPy** (for lattice generation):
   ```bash
   pip install scipy
   ```

5. **PyYAML** (for configuration parsing):
   ```bash
   pip install pyyaml
   ```

6. **IPyWidgets** (for interactive widgets):
   ```bash
   pip install ipywidgets
   ```

7. **PyTorch3D (Optional)**:
   For advanced rendering, install PyTorch3D matching your CUDA version and Python version. For CUDA 11.8 and Python 3.10:
   ```bash
   pip install pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py3.10_cu118_pyt20/index.html
   ```

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/3D-Mesh.git
   cd 3D-Mesh
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts ctivate
   ```

3. **Install Dependencies**:
   Follow the installation steps for the libraries mentioned above.

4. **Run the Program**:
   ```bash
   python program.py
   ```

---

## **Sample Execution**
- **Prompt**: `diamond lattice structure inside of a half open ball`
- **Output**:
  - Generated `.PLY` and `.OBJ` files saved in the working directory.
  - Example filenames:
    - `generated_mesh_0.ply`
    - `generated_mesh_0.obj`

---

## **Known Issues**
1. **PyTorch3D Warnings**:
   - If PyTorch3D is not installed, the program will fall back to the native PyTorch renderer.
   - Warning suppression:
     ```python
     import warnings
     warnings.filterwarnings("ignore", category=UserWarning, module="shap_e")
     ```

2. **CRLF Line Endings**:
   - On Windows, line ending warnings (`LF will be replaced by CRLF`) can appear. To fix:
     ```bash
     git config --global core.autocrlf true
     ```

---

## **Future Enhancements**
1. **Enhanced Lattice Generation**:
   - Add advanced lattice structures such as TPMS.

2. **Integration with Advanced FEA**:
   - Use FEniCS for finite element analysis during lattice optimization.

3. **Custom Prompt Handling**:
   - Improve model adherence to complex prompts.

---

For questions or issues, please open an issue in the repository or contact the maintainer.
