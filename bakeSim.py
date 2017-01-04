from maya import cmds
import maya.mel as mel

class bakeWindow(object):

    windowName = "ExportTools"

    joints = ['Pelvis_01_JNT', 'Thigh_01_L_skin', 'Shin_01_L_skin', 'Foot_01_L_skin', 'Ball_01_L_skin', 'Toe_01_L_skin', 'Shin_01_L_knee_skin', 'Thigh_01_R_skin', 'Shin_01_R_skin', 'Foot_01_R_skin', 'Ball_01_R_skin', 'Toe_01_R_skin', 'spine_1', 'spine_2', 'spine_3', 'spine_4', 'spine_5', 'spine_6', 'spine_7', 'Neck_01_JNT', 'Head_01_JNT', 'Nose_JNT', 'Eye_L_Jnt', 'Eye_R_Jnt', 'Jaw_01_JNT', 'Jaw_01_End', 'Teeth_Bot_Jnt', 'Mid_NoseEndWiggle_JNT', 'L_Ear_A_JNT', 'L_Ear_End', 'L_Cheek_Jaw_JNT', 'L_Cheek_Lower_JNT', 'L_Cheek_Outer_JNT', 'L_EyeShape_Upper_Outer_JNT', 'L_EyeShape_Upper_Mid_JNT', 'L_EyeShape_Upper_Inner_JNT', 'L_EyeShape_Lower_Outer_JNT', 'L_EyeShape_Lower_Mid_JNT', 'L_EyeShape_Lower_Inner_JNT', 'L_Eye_Temple_JNT', 'L_Cheek_Upper_JNT', 'L_Cheek_Inner_JNT', 'L_Nose_Sneer_B_JNT', 'L_Cheek_Mid_JNT', 'L_Nose_Sneer_A_JNT', 'L_Nostril_Flare_JNT', 'Mid_Brow_Upper_JNT', 'Mid_NoseBridgeCrease_JNT', 'Mid_Brow_JNT', 'L_Brow_BoneUpper_A_JNT', 'L_Brow_Outer_JNT', 'L_Brow_Mid_JNT', 'L_Brow_Inner_JNT', 'L_Cheek_MouthOrbit_A_JNT', 'L_Cheek_MouthOrbit_B_JNT', 'Mid_Chin_JNT', 'L_Chin_A_JNT', 'Mid_LowerMouth_Bulge_JNT', 'Mid_UpperMouth_Bulge_JNT', 'L_Cheek_Sneer_JNT', 'L_Jawline_A_JNT', 'L_DoubleChin_Bulge_JNT', 'Mid_DoubleChin_Bulge_JNT', 'L_Eyelid_Outer_JNT', 'L_Eyelid_Inner_JNT', 'L_EyeShape_Outer_JNT', 'L_Brow_BoneUpper_B_JNT', 'L_EyeShape_Inner_JNT', 'L_Eyelid_Top_Mid_Pivot_JNT', 'L_Eyelid_Top_Mid_B_JNT', 'L_Eyelid_Top_outer_Pivot_JNT', 'L_Eyelid_Top_outer_B_JNT', 'L_Eyelid_Top_Inner_Pivot_JNT', 'L_Eyelid_Top_Inner_B_JNT', 'L_Eyelid_Bottom_Mid_Pivot_JNT', 'L_Eyelid_Bottom_Mid_B_JNT', 'L_Eyelid_Bottom_Outer_Pivot_JNT', 'L_Eyelid_Bottom_Outer_B_JNT', 'L_Eyelid_Bottom_Inner_Pivot_JNT', 'L_Eyelid_Bottom_Inner_B_JNT', 'Mid_Lip_Lower_JNT', 'Mid_Lip_Upper_JNT', 'L_Lip_Lower_JNT', 'L_LipCorner_Lower_JNT', 'L_LipCorner_Upper_JNT', 'L_Lip_Upper_JNT', 'L_LipCorner_JNT', 'L_Nose_Sneer_C_JNT', 'L_Nose_Sneer_D_JNT', 'R_Nose_Sneer_D_JNT', 'R_Nose_Sneer_C_JNT', 'R_LipCorner_JNT', 'R_Lip_Upper_JNT', 'R_LipCorner_Upper_JNT', 'R_LipCorner_Lower_JNT', 'R_Lip_Lower_JNT', 'R_Eyelid_Bottom_Inner_Pivot_JNT', 'R_Eyelid_Bottom_Inner_B_JNT', 'R_Eyelid_Bottom_Outer_Pivot_JNT', 'R_Eyelid_Bottom_Outer_B_JNT', 'R_Eyelid_Bottom_Mid_Pivot_JNT', 'R_Eyelid_Bottom_Mid_B_JNT', 'R_Eyelid_Top_Inner_Pivot_JNT', 'R_Eyelid_Top_Inner_B_JNT', 'R_Eyelid_Top_outer_Pivot_JNT', 'R_Eyelid_Top_outer_B_JNT', 'R_Eyelid_Top_Mid_Pivot_JNT', 'R_Eyelid_Top_Mid_B_JNT', 'R_EyeShape_Inner_JNT', 'R_Brow_BoneUpper_B_JNT', 'R_EyeShape_Outer_JNT', 'R_Eyelid_Inner_JNT', 'R_Eyelid_Outer_JNT', 'R_DoubleChin_Bulge_JNT', 'R_Jawline_A_JNT', 'R_Cheek_Sneer_JNT', 'R_Chin_A_JNT', 'R_Cheek_MouthOrbit_B_JNT', 'R_Cheek_MouthOrbit_A_JNT', 'R_Brow_Inner_JNT', 'R_Brow_Mid_JNT', 'R_Brow_Outer_JNT', 'R_Brow_BoneUpper_A_JNT', 'R_Nostril_Flare_JNT', 'R_Nose_Sneer_A_JNT', 'R_Cheek_Mid_JNT', 'R_Nose_Sneer_B_JNT', 'R_Cheek_Inner_JNT', 'R_Cheek_Upper_JNT', 'R_Eye_Temple_JNT', 'R_EyeShape_Lower_Inner_JNT', 'R_EyeShape_Lower_Mid_JNT', 'R_EyeShape_Lower_Outer_JNT', 'R_EyeShape_Upper_Inner_JNT', 'R_EyeShape_Upper_Mid_JNT', 'R_EyeShape_Upper_Outer_JNT', 'R_Cheek_Outer_JNT', 'R_Cheek_Lower_JNT', 'R_Cheek_Jaw_JNT', 'R_Ear_A_JNT', 'R_Ear_End', 'Teeth_Top_Jnt', 'L_Clavicle_skin', 'L_Shoulder_skin', 'L_Forearm_skin', 'L_Wrist_skin', 'L_Thumb_orientjoint2', 'L_Thumb_01', 'L_Thumb_02', 'L_Thumb_03', 'L_Thumb_04', 'L_Thumb_end', 'L_LittleFinger_06', 'L_LittleFinger_02', 'L_LittleFinger_03', 'L_LittleFinger_04', 'L_LittleFinger_end', 'L_RingFinger_06', 'L_RingFinger_02', 'L_RingFinger_03', 'L_RingFinger_04', 'L_RingFinger_end', 'L_IndexFinger_07', 'L_IndexFinger_02', 'L_IndexFinger_03', 'L_IndexFinger_04', 'L_IndexFinger_end', 'L_MiddleFinger_06', 'L_MiddleFinger_02', 'L_MiddleFinger_03', 'L_MiddleFinger_04', 'L_MiddleFinger_end', 'L_Forearm_Twist_skin', 'L_Elbow_Solver_skin', 'R_Clavicle_skin', 'R_Shoulder_skin', 'R_Forearm_skin', 'R_Wrist_skin', 'R_Thumb_orientjoint2', 'R_Thumb_01', 'R_Thumb_02', 'R_Thumb_03', 'R_Thumb_04', 'R_Thumb_end', 'R_LittleFinger_06', 'R_LittleFinger_02', 'R_LittleFinger_03', 'R_LittleFinger_04', 'R_LittleFinger_end', 'R_RingFinger_06', 'R_RingFinger_02', 'R_RingFinger_03', 'R_RingFinger_04', 'R_RingFinger_end', 'R_IndexFinger_07', 'R_IndexFinger_02', 'R_IndexFinger_03', 'R_IndexFinger_04', 'R_IndexFinger_end', 'R_MiddleFinger_06', 'R_MiddleFinger_02', 'R_MiddleFinger_03', 'R_MiddleFinger_04', 'R_MiddleFinger_end', 'R_Forearm_Twist_skin', 'Hoodie_Main_JNT', 'Hoodie01_Jiggle_Joint01', 'Hoodie01_Jiggle_Joint02', 'Hoodie01_Jiggle_Joint_end', 'Hoodie02_Jiggle_Joint01', 'Hoodie02_Jiggle_Joint02', 'Hoodie02_Jiggle_Joint_end', 'Hoodie03_Jiggle_Joint01', 'Hoodie03_Jiggle_Joint02', 'Hoodie03_Jiggle_Joint_end', 'Button02_Jiggle_Joint01', 'Button02_Jiggle_Joint02', 'Button02_Jiggle_Joint_end', 'Button01_Jiggle_Joint01', 'Button01_Jiggle_Joint02', 'Button01_Jiggle_Joint_end', 'Jacket01_Jiggle_Joint01', 'Jacket01_Jiggle_Joint02', 'Jacket01_Jiggle_Joint_end', 'Button03_Jiggle_Joint01', 'Button03_Jiggle_Joint02', 'Button03_Jiggle_Joint_end', 'Jacket02_Jiggle_Joint01', 'Jacket02_Jiggle_Joint02', 'Jacket02_Jiggle_Joint_end']
    ctrls = [u'chest_anim', u'Spine_2_CTRL', u'Spine_1_CTRL', u'Pelvis_anim', u'COG_CTRL', u'L_Hand_CTRL', u'L_Wrist_FK_Anim', u'L_Forearm_FK_Anim', u'L_Shoulder_FK_Anim', u'L_Clav_Anim', u'L_arm_elbow_anim', u'L_Wrist_IK_anim', u'R_Hand_CTRL', u'R_Wrist_FK_Anim', u'R_Forearm_FK_Anim', u'R_Shoulder_FK_Anim', u'R_Clav_Anim', u'R_Wrist_IK_anim', u'R_arm_elbow_anim', u'L_Toe_FK_anim', u'L_Foot_FK_anim', u'L_Shin_FK_anim', u'L_Thigh_FK_anim', u'L_Foot_IK_Anim', u'L_Leg_Knee_anim', u'R_Foot_IK_Anim', u'R_Leg_Knee_anim', u'R_Toe_FK_anim', u'R_Foot_FK_anim', u'R_Shin_FK_anim', u'R_Thigh_FK_anim', u'Mouth_CTRL', u'L_Eye_Shape', u'R_Eye_Shape', u'Nose_CTRL', u'Eye_R_CTRL', u'Eye_L_CTRL', u'Eyes_CTRL', u'R_Eyebrow_CTRL', u'L_Eyebrow_CTRL', u'EyeBrow_Mid_CTRL', u'Jaw_CTRL', u'Head_CTRL', u'Neck_CTRL', u'Teeth_Upper_CTRL', u'Teeth_Lower_CTRL', u'L_LittleFinger03_Anim', u'L_LittleFinger02_Anim', u'L_LittleFinger01_Anim', u'L_Metacarpus_LittleFinger_Anim', u'L_RingFinger03_Anim', u'L_RingFinger02_Anim', u'L_RingFinger01_Anim', u'L_Metacarpus_RingFinger_Anim', u'L_MiddleFinger03_Anim', u'L_MiddleFinger02_Anim', u'L_MiddleFinger01_Anim', u'L_Metacarpus_MiddleFinger_Anim', u'L_ForeFinger03_Anim', u'L_ForeFinger02_Anim', u'L_Metacarpus_ForeFinger_Anim|L_ForeFinger01_Anim|L_ForeFinger01_Anim', u'L_Metacarpus_ForeFinger_Anim', u'L_Thumb03_Anim', u'L_Thumb02_Anim', u'L_Thumb01_Anim', u'L_Metacarpus_Thumb_Anim', u'R_LittleFinger03_Anim', u'R_LittleFinger02_Anim', u'R_LittleFinger01_Anim', u'R_Metacarpus_LittleFinger_Anim', u'R_RingFinger03_Anim', u'R_RingFinger02_Anim', u'R_RingFinger01_Anim', u'R_Metacarpus_RingFinger_Anim', u'R_MiddleFinger03_Anim', u'R_MiddleFinger02_Anim', u'R_MiddleFinger01_Anim', u'R_Metacarpus_MiddleFinger_Anim', u'R_ForeFinger03_Anim', u'R_ForeFinger02_Anim', u'R_Metacarpus_ForeFinger_Anim|R_ForeFinger01_Anim|R_ForeFinger01_Anim', u'R_Metacarpus_ForeFinger_Anim', u'R_Thumb03_Anim', u'R_Thumb02_Anim', u'R_Thumb01_Anim', u'R_Metacarpus_Thumb_Anim']
    mesh = ['Jacket_geo', 'R_Arm_geo', 'L_Arm_geo', 'undershirt_geo', 'Trousers_geo', 'Hoodie_geo', 'Button_01', 'Button_02', 'Button_03', 'R_Hand_geo', 'L_Hand_geo', 'L_Foot_geo', 'R_Foot_geo', 'eyes', 'eye_cornl2', 'Throat_GEO', 'BottomTeethShape', 'TopTeethShape', 'muro_head_CShape']
    locators = []

    def show(self):

        if cmds.window(self.windowName, query=True, exists=True):
            cmds.deleteUI(self.windowName)

        cmds.window(self.windowName)
        self.buildUI()
        cmds.showWindow()

    def buildUI(self):

        column = cmds.columnLayout()

        cmds.text(label="Runs all commands")
        cmds.button(label="Run all", command=self.runall)

        cmds.text(label="Individual steps")
        cmds.text(label="Imports reference and detetes its namespace")
        cmds.button(label="Import References", command=self.delnme)

        cmds.text(label="Bakes keys on selected object")
        cmds.button(label="Bake Selected", command=self.bakeS)
        cmds.text(label="Bakes joints on 'Old man' rig")
        cmds.button(label="Bake Rig", command=self.bakeR)
        cmds.text(label="Deletes controlers")
        cmds.button(label="Delete Ctrls", command=self.delCtrl)
        cmds.text(label="Exports selected")
        cmds.button(label="Export Sel", command=self.exprtsel)
        cmds.text(label="Exports old man rig")
        cmds.button(label="Export old man rig", command=self.exprtrig)

        cmds.button(label="Close", command=self.close)


    #deletes namespace
    def delnme(self, *args):
        #errors if no references in scene
        refnme = cmds.ls(references=True)
        if refnme == []:
            print "No references to import"
        else:
            #gets the name of the namespace by taking the name of the reference and removing the suffix RN
            refnme = cmds.ls(references=True)[0]
            refnme=refnme[:-2]
            print refnme

            #imports the reference
            self.impt()

            #moves the contents of namespace "refnme" to root, then removes namespace
            cmds.namespace (mv=(refnme, ":"), f=True)
            cmds.namespace (removeNamespace=refnme, f=True)

    def impt(self, *args):
        ref = cmds.ls(references=True)
        print ref

        for i in ref:
            rFile = cmds.referenceQuery(i, f=True)
            cmds.file(rFile, importReference=True)

    def bakeR(self, joints, *args):
        print "baking keys of Old Man rig"

        # Gets timeline from scene
        min_time = cmds.playbackOptions(q=True, min=True)
        max_time = cmds.playbackOptions(q=True, max=True)

        cmds.select(self.joints)

        # Bakes keys
        cmds.bakeSimulation(preserveOutsideKeys=False, time=(min_time, max_time), sampleBy=1, disableImplicitControl=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)

        print "bake complete"

    def bakeS(self, *args):
        print "baking keys of selected"

        selection = cmds.ls(selection=True)

        if selection == []:
            print "Nothing selected"

        else:
            # Gets timeline from scene
            min_time = cmds.playbackOptions(q=True, min=True)
            max_time = cmds.playbackOptions(q=True, max=True)

            # Bakes keys
            cmds.bakeSimulation(preserveOutsideKeys=False, time=(min_time, max_time), sampleBy=1, disableImplicitControl=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)

            print "bake complete"

    def delCtrl(self, *args):
        print "deleting controlers"
        cmds.select(self.ctrls)
        cmds.delete(self.ctrls)

    def exprtsel(self, *args):
        selection = cmds.ls(selection=True)

        if selection == []:
            print "Nothing selected"
        else:
            print "Exporting Selection"
        #cmds.select(self.joints)
        #cmds.select(self.mesh)
        #cmds.select(self.locators)
        #cmds.exportEdits(exportSelected=True)

    def exprtrig(self, *args):


        print "starting export"
        xprtls = self.joints
        xprtls.extend(self.mesh)
        xprtls.extend(self.locators)

        cmds.select(xprtls)
        print xprtls

        #my_filename = "cube2.fbx"
        #my_folder = "C:/SomeFolder/scenes"
        #full_file_path = join(my_folder, my_filename).replace('\\', '/')


        cmds.FBXExport('-f','G:/Users/_2016 Work_/Muro Rig_THOR/Export script test/export_test.fbx',['-s'])
        #mel.eval('FBXExport -f G:/Users/_2016 Work_/Muro Rig_THOR/Export script/export_test.fbx -s')
        #cmds.file('G:/Users/_2016 Work_/Muro Rig_THOR/Export script/export_test.fbx', exportSelected=True, type="FBX export")
        print "export complete"

    def runall(self, *args):
        self.delnme()
        self.bakeS()
        self.delCtrl()
        self.exprtrig()

    def close(self, *args):
        cmds.deleteUI(self.windowName)

