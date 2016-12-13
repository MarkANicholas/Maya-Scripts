from maya import cmds

class bakeWindow(object):

    windowName = "BakeWindow"
    joints = cmds.ls(selection=True)

    def show(self):

        if cmds.window(self.windowName, query=True, exists=True):
            cmds.deleteUI(self.windowName)

        cmds.window(self.windowName)
        self.buildUI()
        cmds.showWindow()

    def buildUI(self):

        column = cmds.columnLayout()

        cmds.text(label="Bake animation onto bones")

        cmds.button(label="Bake Rig", command=self.bakeR)
        cmds.button(label="Bake Selected", command=self.bakeS)

        cmds.button(label="Close", command=self.close)


    def bakeR(self, joints, *args):
        print "baking keys of Old Man rig"

        # Gets timeline from scene
        min_time = cmds.playbackOptions(q=True, min=True)
        max_time = cmds.playbackOptions(q=True, max=True)

        cmds.select(self.joints)

        #list of every joint needed to be baked in the rig.
        joints = ['Teeth_Top_Jnt', 'Teeth_Bot_Jnt', 'Pelvis_01_JNT', 'Thigh_01_L_skin', 'Shin_01_L_skin', 'Foot_01_L_skin', 'Ball_01_L_skin', 'Toe_01_L_skin', 'Shin_01_L_knee_skin', 'Thigh_01_R_skin', 'Shin_01_R_skin', 'Foot_01_R_skin', 'Ball_01_R_skin', 'Toe_01_R_skin', 'spine_1', 'spine_2', 'spine_3', 'spine_4', 'spine_5', 'spine_6', 'spine_7', 'Neck_01_JNT', 'Head_01_JNT', 'Nose_JNT', 'Eye_L_Jnt', 'Eye_R_Jnt', 'Jaw_01_JNT', 'Jaw_01_End', 'Mid_NoseEndWiggle_JNT', 'L_Ear_A_JNT', 'L_Cheek_Jaw_JNT', 'L_Cheek_Lower_JNT', 'L_Cheek_Outer_JNT', 'L_EyeShape_Upper_Outer_JNT', 'L_EyeShape_Upper_Mid_JNT', 'L_EyeShape_Upper_Inner_JNT', 'L_EyeShape_Lower_Outer_JNT', 'L_EyeShape_Lower_Mid_JNT', 'L_EyeShape_Lower_Inner_JNT', 'L_Eye_Temple_JNT', 'L_Cheek_Upper_JNT', 'L_Cheek_Inner_JNT', 'L_Nose_Sneer_B_JNT', 'L_Cheek_Mid_JNT', 'L_Nose_Sneer_A_JNT', 'L_Nostril_Flare_JNT', 'Mid_Brow_Upper_JNT', 'Mid_NoseBridgeCrease_JNT', 'Mid_Brow_JNT', 'L_Brow_BoneUpper_A_JNT', 'L_Brow_Outer_JNT', 'L_Brow_Mid_JNT', 'L_Brow_Inner_JNT', 'L_Cheek_MouthOrbit_A_JNT', 'L_Cheek_MouthOrbit_B_JNT', 'Mid_Chin_JNT', 'L_Chin_A_JNT', 'Mid_LowerMouth_Bulge_JNT', 'Mid_UpperMouth_Bulge_JNT', 'L_Cheek_Sneer_JNT', 'L_Jawline_A_JNT', 'L_DoubleChin_Bulge_JNT', 'Mid_DoubleChin_Bulge_JNT', 'L_Eyelid_Outer_JNT', 'L_Eyelid_Inner_JNT', 'L_EyeShape_Outer_JNT', 'L_Brow_BoneUpper_B_JNT', 'L_EyeShape_Inner_JNT', 'L_Eyelid_Top_Mid_Pivot_JNT', 'L_Eyelid_Top_Mid_B_JNT', 'L_Eyelid_Top_outer_Pivot_JNT', 'L_Eyelid_Top_outer_B_JNT', 'L_Eyelid_Top_Inner_Pivot_JNT', 'L_Eyelid_Top_Inner_B_JNT', 'L_Eyelid_Bottom_Mid_Pivot_JNT', 'L_Eyelid_Bottom_Mid_B_JNT', 'L_Eyelid_Bottom_Outer_Pivot_JNT', 'L_Eyelid_Bottom_Outer_B_JNT', 'L_Eyelid_Bottom_Inner_Pivot_JNT', 'L_Eyelid_Bottom_Inner_B_JNT', 'Mid_Lip_Lower_JNT', 'Mid_Lip_Upper_JNT', 'L_Lip_Lower_JNT', 'L_LipCorner_Lower_JNT', 'L_LipCorner_Upper_JNT', 'L_Lip_Upper_JNT', 'L_LipCorner_JNT', 'L_Nose_Sneer_C_JNT', 'L_Nose_Sneer_D_JNT', 'R_Nose_Sneer_D_JNT', 'R_Nose_Sneer_C_JNT', 'R_LipCorner_JNT', 'R_Lip_Upper_JNT', 'R_LipCorner_Upper_JNT', 'R_LipCorner_Lower_JNT', 'R_Lip_Lower_JNT', 'R_Eyelid_Bottom_Inner_Pivot_JNT', 'R_Eyelid_Bottom_Inner_B_JNT', 'R_Eyelid_Bottom_Outer_Pivot_JNT', 'R_Eyelid_Bottom_Outer_B_JNT', 'R_Eyelid_Bottom_Mid_Pivot_JNT', 'R_Eyelid_Bottom_Mid_B_JNT', 'R_Eyelid_Top_Inner_Pivot_JNT', 'R_Eyelid_Top_Inner_B_JNT', 'R_Eyelid_Top_outer_Pivot_JNT', 'R_Eyelid_Top_outer_B_JNT', 'R_Eyelid_Top_Mid_Pivot_JNT', 'R_Eyelid_Top_Mid_B_JNT', 'R_EyeShape_Inner_JNT', 'R_Brow_BoneUpper_B_JNT', 'R_EyeShape_Outer_JNT', 'R_Eyelid_Inner_JNT', 'R_Eyelid_Outer_JNT', 'R_DoubleChin_Bulge_JNT', 'R_Jawline_A_JNT', 'R_Cheek_Sneer_JNT', 'R_Chin_A_JNT', 'R_Cheek_MouthOrbit_B_JNT', 'R_Cheek_MouthOrbit_A_JNT', 'R_Brow_Inner_JNT', 'R_Brow_Mid_JNT', 'R_Brow_Outer_JNT', 'R_Brow_BoneUpper_A_JNT', 'R_Nostril_Flare_JNT', 'R_Nose_Sneer_A_JNT', 'R_Cheek_Mid_JNT', 'R_Nose_Sneer_B_JNT', 'R_Cheek_Inner_JNT', 'R_Cheek_Upper_JNT', 'R_Eye_Temple_JNT', 'R_EyeShape_Lower_Inner_JNT', 'R_EyeShape_Lower_Mid_JNT', 'R_EyeShape_Lower_Outer_JNT', 'R_EyeShape_Upper_Inner_JNT', 'R_EyeShape_Upper_Mid_JNT', 'R_EyeShape_Upper_Outer_JNT', 'R_Cheek_Outer_JNT', 'R_Cheek_Lower_JNT', 'R_Cheek_Jaw_JNT', 'R_Ear_A_JNT', 'L_Clavicle_skin', 'L_Shoulder_skin', 'L_Forearm_skin', 'L_Wrist_skin', 'group2', 'L_Thumb_orientjoint2', 'L_Thumb_01', 'L_Thumb_02', 'L_Thumb_03', 'L_Thumb_04', 'L_LittleFinger_06', 'L_LittleFinger_02', 'L_LittleFinger_03', 'L_LittleFinger_04', 'L_RingFinger_06', 'L_RingFinger_02', 'L_RingFinger_03', 'L_RingFinger_04', 'L_IndexFinger_07', 'L_IndexFinger_02', 'L_IndexFinger_03', 'L_IndexFinger_04', 'L_MiddleFinger_06', 'L_MiddleFinger_02', 'L_MiddleFinger_03', 'L_MiddleFinger_04', 'L_Forearm_Twist_skin', 'L_Elbow_Solver_skin', 'R_Clavicle_skin', 'R_Shoulder_skin', 'R_Forearm_skin', 'R_Wrist_skin', 'R_Thumb_orientjoint2', 'group3', 'R_Thumb_01', 'R_Thumb_02', 'R_Thumb_03', 'R_Thumb_04', 'R_LittleFinger_06', 'R_LittleFinger_02', 'R_LittleFinger_03', 'R_LittleFinger_04', 'R_RingFinger_06', 'R_RingFinger_02', 'R_RingFinger_03', 'R_RingFinger_04', 'R_IndexFinger_07', 'R_IndexFinger_02', 'R_IndexFinger_03', 'R_IndexFinger_04', 'R_MiddleFinger_06', 'R_MiddleFinger_02', 'R_MiddleFinger_03', 'R_MiddleFinger_04', 'R_Forearm_Twist_skin', 'R_Elbow_Solver_skin', 'Hoodie_Main_JNT', 'Hoodie01_Jiggle_Joint01', 'Hoodie01_Jiggle_Joint02', 'Hoodie01_Jiggle_Joint_end', 'Hoodie02_Jiggle_Joint01', 'Hoodie02_Jiggle_Joint02', 'Hoodie02_Jiggle_Joint_end', 'Hoodie03_Jiggle_Joint01', 'Hoodie03_Jiggle_Joint02', 'Hoodie03_Jiggle_Joint_end', 'Button02_Jiggle_Joint01', 'Button02_Jiggle_Joint02', 'Button02_Jiggle_Joint_end', 'Button01_Jiggle_Joint01', 'Button01_Jiggle_Joint02', 'Button01_Jiggle_Joint_end', 'Jacket01_Jiggle_Joint01', 'Jacket01_Jiggle_Joint02', 'Jacket01_Jiggle_Joint_end', 'Button03_Jiggle_Joint01', 'Button03_Jiggle_Joint02', 'Button03_Jiggle_Joint_end', 'Jacket02_Jiggle_Joint01', 'Jacket02_Jiggle_Joint02', 'Jacket02_Jiggle_Joint_end', 'spineBase_joint', 'spineChest_joint']

        # Bakes keys
        cmds.bakeSimulation(preserveOutsideKeys=False, time=(min_time, max_time), sampleBy=1, disableImplicitControl=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)

        print "bake complete"

    def bakeS(self, joints, *args):
        print "baking keys of selected"

        # Gets timeline from scene
        min_time = cmds.playbackOptions(q=True, min=True)
        max_time = cmds.playbackOptions(q=True, max=True)

        #adds selection to list called joints

        cmds.select(self.joints)

        # Bakes keys
        cmds.bakeSimulation(preserveOutsideKeys=False, time=(min_time, max_time), sampleBy=1, disableImplicitControl=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)

        print "bake complete"



    def close(self, *args):
        cmds.deleteUI(self.windowName)
