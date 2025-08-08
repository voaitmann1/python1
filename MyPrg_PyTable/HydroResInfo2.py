#p=2*pi*R=pi*D
#S=pi*R*R=pi*D*D/4
#S/p=R/2=D/4=>D=4S/p

from MyMathLib import *

#class HydroResInfo:
    #//{
    #//}
class HydroResistanceConsts:
    HydroRes_vis_FrameElementLeft = "    :....."
    HydroRes_vis_FrameElementRight = "....:     "
    HydroRes_vis_FrameElementVertical = "    :     "
    HydroRes_vis_FrameElementHorisontal = ".........."
    HydroRes_vis_FrameName = ".. Rs___.."
    HydroRes_vis_ConnectorCentral = "----|-----"
    HydroRes_vis_ConnectorLeft = "    |-----"
    HydroRes_vis_ConnectorRight = "----|     "
    HydroRes_vis_LineVertical = "    |     "
    HydroRes_vis_LineHorisontal = "----------"
    HydroRes_vis_LineFrameIntersection = "----:-----"
    HydroRes_vis_ResistanceElementar = "-[ Re___]-"
    HydroRes_vis_ResistanceLeftSide = "----:     "
    HydroRes_vis_ResistanceRightSide = "    :-----"
        #//
        #//
    HydroRes_const_g_fall_acc = 9.81
        #//public const int QParallelHydroResistancesMax = 16
    HydroRes_const_LocResistanceGroupN = 1
    HydroRes_const_WayResistanceGroupN = 2
    HydroRes_const_LocResistanceGroupName_En = "Loc."
    HydroRes_const_LocResistanceGroupName = "ћестн."
    HydroRes_const_WayResistanceGroupName_En = "Way."
    HydroRes_const_WayResistanceGroupName = "ѕут."
        #//
        #//
    HydroRes_const_ResistanceLocConstResistCoefSubTypeN = 1
    HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN = 2
    HydroRes_const_ResistanceLocFlowDependentResistCoefSubTypeN = 3
        #//
        #//
    HydroRes_const_ResistanceTypeN_Loc_Simple_TJointUniting = 4
        #//
    HydroRes_const_ResistanceTypeN_Loc_Simple_SuddBroad = 4
    HydroRes_const_ResistanceTypeN_Loc_Simple_SuddNarr = 5
    HydroRes_const_ResistanceTypeN_Loc_Simple_GradBroad = 4
    HydroRes_const_ResistanceTypeN_Loc_Simple_GradNarr = 5
        #//
    HydroRes_const_ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline = "¬ход»зЅака"
    HydroRes_const_ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline_En = "InletFromSpace"
    HydroRes_const_ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline = 1
    HydroRes_const_ResistanceCoefVal_min_InletFromSpaceToPipeline = 0.5
    HydroRes_const_ResistanceCoefVal_max_InletFromSpaceToPipeline = 0.5
    HydroRes_const_ResistanceCoefVal_InletFromSpaceToPipeline = 0.5#;//1?
    HydroRes_const_DefWay_InletFromSpaceToPipeline_Const0ConstsRange1TableStdParams2TableSpecParams3 = 0
        #//
    HydroRes_const_ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace = "¬ыход¬Ѕак"
    HydroRes_const_ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace_En = "OutletToSpace"
    HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace = 2
    HydroRes_const_ResistanceCoefVal_min_OutletFromPilelineToSpace = 1#;//0.5?
    HydroRes_const_ResistanceCoefVal_max_OutletFromPilelineToSpace = 1#;//0.5?
    HydroRes_const_ResistanceCoefVal_OutletFromPilelineToSpace = 1#;//0.5?
    HydroRes_const_DefWay_OutletFromPilelineToSpace_Const0ConstsRange1TableStdParams2TableSpecParams3 = 0
        #//
       # //public const string ResistanceTypeName_Loc_Simple_TJoint = "TJoint"
    HydroRes_const_ResistanceTypeName_Loc_Simple_TJoint = "“ройник"
    HydroRes_const_ResistanceTypeName_Loc_Simple_TJoint_En = "TJoint"
    HydroRes_const_ResistanceTypeN_Loc_Simple_TJoint = 3
    HydroRes_const_ResistanceCoefVal_Simple_TJoint = 2#;//0.5?
    HydroRes_const_ResistanceCoefVal_max_Simple_TJoint = 1.5#;//0.5?
    HydroRes_const_ResistanceCoefVal_min_Simple_TJoint = 2.5#;//0.5?
    HydroRes_const_DefWay_Simple_TJoint_Const0ConstsRange1TableStdParams2TableSpecParams3 = 1
        #//
    HydroRes_const_ResistanceTypeName_Loc_Simple_DuriteSchlange = "ƒюрит.шланг"
    HydroRes_const_ResistanceTypeName_Loc_Simple_DuriteSchlange_En = "DuriteSchlange"
    HydroRes_const_esistanceTypeN_Loc_Simple_DuriteSchlange = 5
    HydroRes_const_ResistanceCoefVal_DuriteSchlange = 0.25#;//0.5?
    HydroRes_const_ResistanceCoefVal_max_DuriteSchlange = 0.2#;//0.5?
    HydroRes_const_ResistanceCoefVal_min_DuriteSchlange = 0.3#;//0.5?
    HydroRes_const_DefWay_DuriteSchlange_Const0ConstsRange1TableStdParams2TableSpecParams3 = 1
        #//
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddBroad = "–езк.расшир"#;//"SuddBroad."
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddBroad_En = "SuddBroad."
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddBroad = "SuddBroad."
    HydroRes_const_ResistanceCoefVal_SuddBroad = 0
    HydroRes_const_ResistanceCoefVal_max_SuddBroad = 0
    HydroRes_const_ResistanceCoefVal_min_SuddBroad = 0
    HydroRes_const_ResistanceTypeN_Loc_Geom_SuddBroad = 10
        #//
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddNarr = "–езк.сужение"#;//table
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddNarr_En = "SuddNarr"
    HydroRes_const_ResistanceCoefVal_SuddNarr = 0
    HydroRes_const_ResistanceCoefVal_max_SuddNarr = 0
    HydroRes_const_ResistanceCoefVal_min_SuddNarr = 0
    HydroRes_const_ResistanceTypeN_Loc_Geom_SuddNarr = 20
        #//
       # //public const string ResistanceTypeName_Loc_Geom_SuddTurn90Deg = "SuddTurn90Deg."
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn90 = "–езкѕовор90град"
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn90_En = "SuddTurn90"
    HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn90 = 30
    HydroRes_const_ResistanceCoefVal_Loc_Geom_SuddTurn90 = 0
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_SuddTurn90 = 0
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_SuddTurn90 = 0
        #//
        #//public const string ResistanceTypeName_Loc_Geom_SuddTurn = "SuddTurn."
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn = "–езк.поворот"#;//graph
    HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn_En = "SuddTurn"
    HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn = 40
    HydroRes_const_ResistanceCoefVal_Loc_Geom_SuddTurn = 0
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_SuddTurn = 0
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_SuddTurn = 0
        #//
        #//public const string ResistanceTypeName_Loc_Geom_GradTurn = "GradTurn."
    HydroRes_const_ResistanceTypeName_Loc_Geom_GradTurn = "ѕлавн.поворот"
    HydroRes_const_ ResistanceTypeName_Loc_Geom_GradTurn_En = "GradTurn"
    HydroRes_const_ResistanceTypeN_Loc_Geom_GradTurn = 50
    HydroRes_const_ResistanceCoefVal_Loc_Geom_GradTurn = 0
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_GradTurn = 0
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_GradTurn = 0
        #//
        #//public const string ResistanceTypeName_Loc_Geom_GradBroad = "Diffusor"
    HydroRes_const_ResistanceTypeName_Loc_Geom_GradBroad = "ѕлавн.расшир"#;//;02=. 0AH8@.
    HydroRes_const_ResistanceTypeName_Loc_Geom_GradBroad_En = "GradBroad"
    HydroRes_const_ResistanceTypeN_Loc_Geom_GradBroad = 60
    HydroRes_const_ResistanceCoefVal_Loc_Geom_GradBroad = 0
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_GradBroad = 0
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_GradBroad = 0
        #//
        #//public const string ResistanceTypeName_Loc_Geom_GradNarr = "Confusor"
    HydroRes_const_ResistanceTypeName_Loc_Geom_GradNarr = "ѕлавн.сужение"#;//;02=.!C65=85.
    HydroRes_const_ResistanceTypeName_Loc_Geom_GradNarr_En = "GradNarr"
    HydroRes_const_ResistanceTypeN_Loc_Geom_GradNarr = 70
    HydroRes_const_ResistanceCoefVal_Loc_Geom_GradNarr = 0
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_GradNarr = 0
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_GradNarr = 0
    #     //
    #     //public const string ResistanceTypeName_Loc_Geom_Schieber = "Schieber";
    HydroRes_const_ResistanceTypeName_Loc_Geom_Schieber = "Ўибер"#;//0A;>=:0!4286=0O.//table - % of closing
    HydroRes_const_ResistanceTypeName_Loc_Geom_Schieber_En = "Schieber";
    HydroRes_const_ResistanceTypeN_Loc_Geom_Schieber = 80;
    HydroRes_const_ResistanceCoefVal_Loc_Geom_Schieber =0;
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_Schieber = 0;
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_Schieber = 0;
    #     //
    #     //public const string ResistanceTypeName_Loc_Geom_DrosselTurningThrottle = "Throttle";
    HydroRes_const_ResistanceTypeName_Loc_Geom_DrosselTurningThrottle = "ƒроссельна€«аслонка"; //turn angle
    HydroRes_const_ResistanceTypeName_Loc_Geom_DrosselTurningThrottle_En = "DrosselTurningThrottle";
    HydroRes_const_ResistanceTypeN_Loc_Geom_DrosselTurningThrottle = 90;
    HydroRes_const_ResistanceCoefVal_Loc_DrosselTurningThrottle = 0;
    HydroRes_const_ResistanceCoefVal_max_Loc_DrosselTurningThrottle = 0;
    HydroRes_const_ResistanceCoefVal_min_Loc_DrosselTurningThrottle = 0;
    #     //
    #     //public const string ResistanceTypeName_Loc_Geom_DiaphragmAcute = "DiaphragmAcute";//acute diaphragm
    HydroRes_const_ResistanceTypeName_Loc_Geom_DiaphragmAcute = "ƒиафрагмаќстр";//AB@0O 480D@03<0
    HydroRes_const_ResistanceTypeName_Loc_Geom_DiaphragmAcute_En = "DiaphragmAcute";
    HydroRes_const_ResistanceTypeN_Loc_Geom_DiaphragmAcute = 110;
    HydroRes_const_esistanceCoefVal_Loc_Geom_DiaphragmAcute = 0;
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_DiaphragmAcute = 0;
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_DiaphragmAcute =0;
    #    //
    #     //public const string ResistanceTypeName_Loc_Geom_FlowMeter = "FlowMeter";// 0AE>4><5@.
    HydroRes_const_ResistanceTypeName_Loc_Geom_FlowMeter = "–асходомер";// 0AE>4><5@.
    HydroRes_const_ResistanceTypeName_Loc_Geom_FlowMeter_En = "FlowMeter";
    HydroRes_const_ResistanceTypeN_Loc_Geom_FlowMeter = 120;// 0AE>4><5@.
    HydroRes_const_ResistanceCoefVal_Loc_Geom_FlowMeter = 8.5;
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_FlowMeter = 10;
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_FlowMeter = 7;
    #     //
    #     //public const string ResistanceTypeName_Loc_Geom_SelfLockngConnection = "SlfLockConnect";//!0<>70?>@=>5 A>548=5=85.
    HydroRes_const_ResistanceTypeName_Loc_Geom_SelfLockngConnection = "—амозапорн.соед";//!0<>70?>@=>5 A>548=5=85.
    HydroRes_const_ResistanceTypeName_Loc_Geom_SelfLockngConnection_En = "SelfLockingConnection";
    HydroRes_const_ResistanceTypeN_Loc_Geom_SelfLockngConnection = 130;
    HydroRes_const_ResistanceCoefVal_Loc_Geom_SelfLockngConnection = 2.25;
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_SelfLockngConnection = 2.5;
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_SelfLockngConnection = 2;
    #     //
    #     //public const string ResistanceTypeName_Loc_Geom_StopCock = "StopCock";//0?>@=K9 :@0=.
    HydroRes_const_ ResistanceTypeName_Loc_Geom_StopCock = " ран«апорный";//0?>@=K9 :@0=.
    HydroRes_const_ResistanceTypeName_Loc_Geom_StopCock_En = "StopCock";
    HydroRes_const_ResistanceTypeN_Loc_Geom_StopCock = 140;
    HydroRes_const_ResistanceCoefVal_Loc_Geom_StopCock = 2.25;
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_StopCock = 2.5;
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_StopCock = 1;
    #     //
    HydroRes_const_ResistanceTypeName_Loc_Geom_CheckValve = "ќбратный клапан";//1@0B=K9;0?0=.
    HydroRes_const_ResistanceTypeName_Loc_Geom_CheckValve_En = "CheckValve";
    HydroRes_const_ResistanceTypeN_Loc_Geom_CheckValve = 150;
    HydroRes_const_ResistanceCoefVal_Loc_Geom_CheckValve = 1.85;
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_CheckValve = 2;
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_CheckValve = 1.7;
    #     //public const double ResistanceCoef_val_Loc_Geom_CheckValve = 2.5;//?
    #$     //
    HydroRes_const_ResistanceTypeName_Loc_Geom_Valve = " лапан";//1@0B=K9;0?0=.
    HydroRes_const_ResistanceTypeName_Loc_Geom_Valve_En = "Valve";
    HydroRes_const_ResistanceTypeN_Loc_Geom_Valve = 160;
    HydroRes_const_ResistanceCoefVal_Loc_Geom_Valve =0;
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_Valve = 0;
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_Valve = 0;
    #     //
    #     //public const string ResistanceTypeName_Loc_Geom_TransferValve = "TransferValve";//5@52>4=>9;0?0=.
    HydroRes_const_ResistanceTypeName_Loc_Geom_TransferValve = "ѕерепуск.клапан"#;//5@52>4=>9;0?0=.
    HydroRes_const_ResistanceTypeName_Loc_Geom_TransferValve_En = "TransferValve"
    HydroRes_const_ResistanceTypeN_Loc_Geom_TransferValve = 170
    HydroRes_const_ResistanceCoefVal_Loc_Geom_TransferValve = 1.85
    HydroRes_const_ResistanceCoefVal_max_Loc_Geom_TransferValve = 2
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_TransferValve = 1.7
    #     //
    HydroRes_const_ResistanceCoef_val_Loc_Geom_TransferValve = 2#;//such const //const given in table
    #    //public const string ResistanceTypeName_Loc_Geom_StrainerFilter = "Strainer";//!5BG0BK9$8;LB@.
    HydroRes_const_ResistanceTypeName_Loc_Geom_StrainerFilter = "‘ильтр";//!5BG0BK9$8;LB@.
    HydroRes_const_ResistanceTypeName_Loc_Geom_StrainerFilter_En = "StrainerFilter";
    HydroRes_const_ResistanceTypeN_Loc_Geom_StrainerFilter = 180
    HydroRes_const_ResistanceCoefVal_Loc_Geom_StrainerFilter = 1.75
    HydroRes_const_ ResistanceCoefVal_max_Loc_Geom_StrainerFilter = 2.5
    HydroRes_const_ResistanceCoefVal_min_Loc_Geom_StrainerFilter = 1.5
    #    //
    #    //
    #    //public const string TubeInnerSurfaceMatAndQua_Name_Glass = "Glass";
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_Glass = "—текло"
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_Glass_En = "Glass"
    HydroRes_const_TubeInnerSurfaceMatAndQua_N_Glass = 1
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_Glass = 0
    HydroRes_const_ TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_min_Glass = 0
    HydroRes_const_ TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_max_Glass = 0
    #    //public const string TubeInnerSurfaceMatAndQua_Name_PipesDrawnOfBrassOrCopper = "PipesDrawnBrassCopper";//TubesGezogenAusCuprum
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_PipesDrawnOfBrassOrCopper_En = "PipesDrawnBrassCopper"
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_PipesDrawnOfBrassOrCopper = "ћедные трубы"
    HydroRes_const_TubeInnerSurfaceMatAndQua_N_PipesDrawnOfBrassOrCopper = 2
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_PipesDrawnOfBrassOrCopper = 0.001
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_min_PipesDrawnOfBrassOrCopper = 0
    HydroRes_const_ TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_max_PipesDrawnOfBrassOrCopper = 0.002
    #    //public const string TubeInnerSurfaceMatAndQua_Name_HiQuaSteelSeamlessTubes = "HiQuaSteelSeamlessTubes";
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_HiQuaSteelSeamlessTubes_En = "HiQuaSteelSeamlessTubes"
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_HiQuaSteelSeamlessTubes = "¬ыс ачЌерж“рубы"
    HydroRes_const_TubeInnerSurfaceMatAndQua_N_HiQuaSteelSeamlessTubes = 3
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_HiQuaSteelSeamlessTubes = 0.13
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_min_HiQuaSteelSeamlessTubes = 0.06
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_max_HiQuaSteelSeamlessTubes = 0.2
    #    //public const string TubeInnerSurfaceMatAndQua_Name_SteelTubes = "SteelTubes";
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_SteelTubes_En = "SteelTubes"
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_SteelTubes = "—тальн“рубы"
    HydroRes_const_TubeInnerSurfaceMatAndQua_N_SteelTubes = 4;
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_SteelTubes = 0.35
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_min_SteelTubes = 0.5
    HydroRes_const_ TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_max_SteelTubes = 0.1
    #    //public const string TubeInnerSurfaceMatAndQua_Name_CastIronAsphaltTubes = "CastIronAsphaltTubes";
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_CastIronAsphaltTubes_En = "CastIronAsphaltTubes"
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_CastIronAsphaltTubes = "„угуннјсфальт“рубы"
    HydroRes_const_TubeInnerSurfaceMatAndQua_N_CastIronAsphaltTubes = 5
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_CastIronAsphaltTubes = 0.15
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_min_CastIronAsphaltTubes = 0.1
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_max_CastIronAsphaltTubes = 0.2
    #    //public const string TubeInnerSurfaceMatAndQua_Name_CastIronTubes = "CastIronTubes";
    HydroRes_const_ TubeInnerSurfaceMatAndQua_Name_CastIronTubes_En = "CastIronTubes"
    HydroRes_const_TubeInnerSurfaceMatAndQua_Name_CastIronTubes = "„угуннЋитые“рубы"
    HydroRes_const_TubeInnerSurfaceMatAndQua_N_CastIronTubes = 6
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_CastIronTubes = 0.06
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_min_CastIronTubes = 0.2
    HydroRes_const_TubeInnerSurfaceMatAndQua_CoefDeltaEqvVal_max_CastIronTubes = 1.0
    #    //
    #    
    #    //
    HydroRes_ConstArray_TubeInnerSurfaceMatAndQua_ItemNames =[
            HydroRes_const_TubeInnerSurfaceMatAndQua_Name_Glass,
            HydroRes_const_TubeInnerSurfaceMatAndQua_Name_PipesDrawnOfBrassOrCopper,
            HydroRes_const_TubeInnerSurfaceMatAndQua_Name_HiQuaSteelSeamlessTubes,
            HydroRes_const_TubeInnerSurfaceMatAndQua_Name_SteelTubes,
            HydroRes_const_TubeInnerSurfaceMatAndQua_Name_CastIronAsphaltTubes,
            HydroRes_const_TubeInnerSurfaceMatAndQua_Name_CastIronTubes
    ]
    HydroRes_ConstArray_TubeInnerSurfaceMatAndQua_ItemNs = [
            HydroRes_const_TubeInnerSurfaceMatAndQua_N_Glass,
            HydroRes_const_TubeInnerSurfaceMatAndQua_N_PipesDrawnOfBrassOrCopper,
            HydroRes_const_TubeInnerSurfaceMatAndQua_N_HiQuaSteelSeamlessTubes,
            HydroRes_const_TubeInnerSurfaceMatAndQua_N_SteelTubes,
            HydroRes_const_TubeInnerSurfaceMatAndQua_N_CastIronAsphaltTubes,
            HydroRes_const_TubeInnerSurfaceMatAndQua_N_CastIronTubes
    ]
    #    //
    HydroRes_ConstArray_HydroResistancesGroups_ItemNames =[
            LocResistanceGroupName, WayResistanceGroupName
    ]
    HydroRes_ConstArray_HydroResistancesGroups_ItemNs =[
            1, 2
    ]
    #     //
    HydroRes_ConstArray_HydroResistancesLocal_Types_ItemNames =[
       HydroRes_const_ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline,
       HydroRes_const_ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace,
       HydroRes_const_ResistanceTypeName_Loc_Simple_TJoint,
       HydroRes_const_ResistanceTypeName_Loc_Simple_DuriteSchlange,
       HydroRes_const_ResistanceTypeName_Loc_Geom_SuddBroad,
       HydroRes_const_ResistanceTypeName_Loc_Geom_SuddNarr,
       HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn90,
       HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn,
       HydroRes_const_ResistanceTypeName_Loc_Geom_GradBroad,
       HydroRes_const_ResistanceTypeName_Loc_Geom_GradNarr,
       HydroRes_const_ResistanceTypeName_Loc_Geom_Schieber,
       HydroRes_const_ResistanceTypeName_Loc_Geom_DrosselTurningThrottle,
       #//ResistanceTypeName_Loc_Geom_Valve,
       HydroRes_const_ResistanceTypeName_Loc_Geom_DiaphragmAcute,
       HydroRes_const_ResistanceTypeName_Loc_Geom_FlowMeter,
       HydroRes_const_ResistanceTypeName_Loc_Geom_SelfLockngConnection,
       HydroRes_const_ResistanceTypeName_Loc_Geom_StopCock,
       HydroRes_const_ResistanceTypeName_Loc_Geom_CheckValve,
       HydroRes_const_ResistanceTypeName_Loc_Geom_Valve,
       HydroRes_const_ResistanceTypeName_Loc_Geom_TransferValve,
       HydroRes_const_ResistanceTypeName_Loc_Geom_StrainerFilter
    ]
    HydroRes_ConstArray_HydroResistancesLocal_Types_ItemNames_En =[
        HydroRes_const_ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline_En,
        HydroRes_const_ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace_En,
        HydroRes_const_ResistanceTypeName_Loc_Simple_TJoint_En,
        HydroRes_const_ResistanceTypeName_Loc_Simple_DuriteSchlange_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_SuddBroad_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_SuddNarr_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn90_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_GradBroad_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_GradNarr_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_Schieber_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_DrosselTurningThrottle_En,
        #//ResistanceTypeName_Loc_Geom_Valve_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_DiaphragmAcute_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_FlowMeter_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_SelfLockngConnection_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_StopCock_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_CheckValve_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_Valve_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_TransferValve_En,
        HydroRes_const_ResistanceTypeName_Loc_Geom_StrainerFilter_En
    ]
    HydroRes_ConstArray_HydroResistancesLocal_Types_ItemNs =[
        HydroRes_const_esistanceTypeN_Loc_Simple_InletFromSpaceToPipeline,
        HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace,
        HydroRes_const_ResistanceTypeN_Loc_Simple_TJoint,
        HydroRes_const_ResistanceTypeN_Loc_Simple_DuriteSchlange,
        HydroRes_const_ResistanceTypeN_Loc_Geom_SuddBroad,
        HydroRes_const_ResistanceTypeN_Loc_Geom_SuddNarr,
        HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn90,
        HydroRes_const_ ResistanceTypeN_Loc_Geom_SuddTurn,
        HydroRes_const_ResistanceTypeN_Loc_Geom_GradBroad,
        HydroRes_const_ResistanceTypeN_Loc_Geom_GradNarr,
        HydroRes_const_ResistanceTypeN_Loc_Geom_Schieber,
        HydroRes_const_ResistanceTypeN_Loc_Geom_DrosselTurningThrottle,
        #//ResistanceTypeN_Loc_Geom_Valve,
        HydroRes_const_ResistanceTypeN_Loc_Geom_DiaphragmAcute,
        HydroRes_const_ResistanceTypeN_Loc_Geom_FlowMeter,
        HydroRes_const_ResistanceTypeN_Loc_Geom_SelfLockngConnection,
        HydroRes_const_ResistanceTypeN_Loc_Geom_StopCock,
        HydroRes_const_ResistanceTypeN_Loc_Geom_CheckValve,
        HydroRes_const_ResistanceTypeN_Loc_Geom_Valve,
        HydroRes_const_ResistanceTypeN_Loc_Geom_TransferValve,
        HydroRes_const_ResistanceTypeN_Loc_Geom_StrainerFilter
    ]
    #   //
    #   //
    HydroRes_ConstArray_CoefTable_SuddenTurnTo90Deg__x_alfa = [ 30, 60, 90, 120, 180 ]
    HydroRes_ConstArray_CoefTable_SuddenTurnTo90Deg__y_dzeta = [ 0.60, 1, 1.2, 1.4, 1.7 ]
    HydroRes_ConstArray_CoefGraph_SuddenTurnTo90Deg__x_alfa__ByDiagr_v1 = { 0, 20, 37, 40, 50, 60, 70, 76, 80, 90, 98, 100, 101.5, 102 };
    HydroRes_ConstArray_CoefGraph_SuddenTurnTo90Deg__y_dzeta__ByDiagr_v1 = { 0, 0.125, 0.25, 0.3, 0.4, 0.5, 0.65, 0.75, 0.78, 1, 1.25, 1.42, 1.5, 1.58 };
    #//public static double[] CoefGraph_SuddenTurn__x_alfa = {  };
    #//public static double[] CoefGraph_SuddenTurn__y_dzeta = { };
    HydroRes_ConstArray_CoefTable_SuddenTurn__x_alfa__RectChannelTable = { 30, 60, 90, 120, 150, 180};
    HydroRes_ConstArray_CoefTable_SuddenTurn__y_dzeta__RectChannelTable = { 0.5, 0.8, 1, 1.2, 1.3, 1.4};
    HydroRes_ConstArray_CoefTable_GradualTurnTo90Deg__x_r_to_d = [ 0.5, 0.75, 1, 2, 5 ]
    HydroRes_ConstArray_CoefTable_GradualTurnTo90Deg__y_dzeta = [ 1.2, 0.38, 0.19, 0.12, 0.08 ]
    HydroRes_ConstArray_CoefTable_GradualTurn_From90ToAnyDegK__theta = [ 30, 60, 90, 120, 150, 180 ]
    HydroRes_ConstArray_CoefTable_GradualTurn_From90ToAnyDegK__y_K = [ 0.5, 0.8, 1, 1.2, 1.3, 1.5 ]
    HydroRes_ConstArray_CoefTable_SuddenBroadening__F2ToF1 = [ 0.1, 0.5, 0.9 ] #may be not needed
    HydroRes_ConstArray_CoefTable_SuddenBroadening__y_dzeta = [ 0.8, 0.3, 0.01 ] #may be not needed
    HydroRes_ConstArray_CoefTable_SuddenNarrowing__F1ToF2 = [ 0.1, 0.5, 0.9 ] #may be not needed
    HydroRes_ConstArray_CoefTable_SuddenNarrowing__y_dzeta = [ 0.5, 0.3, 0.1 ] #may be not needed
    HydroRes_ConstArray_CoefTable_GradualBroadening_FromSuddenToGradual__x_alfa = [ 4, 8, 15, 30, 60 ] #may be not needed
    HydroRes_ConstArray_CoefTable_GradualBroadening_FromSuddenToGradual__y_K = [ 0.08, 0.16, 0.35, 0.8, 0.95 ] #may be not needed
    #    //
    #    //
    HydroRes_ConstArray_Length = [ 12, 12, 14, 16, 13, 11 ]
    HydroRes_ConstArray_delta = [ 4E-4, 2E-3, 4E-3, 8.3E-3, 0.016, 0.033 ]
    #    //
    HydroRes_ConstArray_x_lg_Re_1 = [ 2.655, 3.325, 3.502, 3.625, 4.891, 4.994, 5.307, 5.393, 5.767, 5.8, 5.87, 6.046 ]
    HydroRes_ConstArray_y_lg_1000_lambda_1 = [ 1.107, 0.452, 0.584, 0.593, 0.276, 0.261, 0.25, 0.261, 0.291, 0.287, 0.294, 0.294 ]
    HydroRes_ConstArray_x_lg_Re_2 = [ 2.655, 3.325, 3.502, 3.625, 4.527, 4.823, 5, 5.236, 5.393, 5.642, 5.8, 6.046 };
    HydroRes_ConstArray_y_lg_1000_lambda_2 = [ 1.107, 0.452, 0.584, 0.593, 0.369, 0.328, 0.321, 0.357, 0.358, 0.373, 0.373, 0.381 ]
    HydroRes_ConstArray_x_lg_Re_3 = [ 2.655, 3.325, 3.502, 3.625, 4.2, 4.481, 4.6, 4.74, 5, 5.22, 5.4, 5.594, 5.8, 6.046 };
    HydroRes_ConstArray_y_lg_1000_lambda_3 = [ 1.107, 0.452, 0.584, 0.593, 0.454, 0.402, 0.401, 0.398, 0.428, 0.446, 0.451, 0.448, 0.446, 0.459 ]
    HydroRes_ConstArray_ x_lg_Re_4 = [ 2.655, 3.325, 3.502, 3.625, 4.038, 4.2, 4.364, 4.6, 4.895, 5, 5.12, 5.4, 5.431, 5.587, 5.8, 6.046 ]
    HydroRes_ConstArray_y_lg_1000_lambda_4 = [ 1.107, 0.452, 0.584, 0.593, 0.493, 0.481, 0.481, 0.501, 0.536, 0.539, 0.552, 0.562, 0.564, 0.549, 0.553, 0.558 ]
    HydroRes_ConstArray_x_lg_Re_5 = [ 2.655, 3.325, 3.502, 3.625, 3.8, 3.876, 4.155, 4.2, 4.372, 4.6, 4.787, 5, 6.046 ]
    HydroRes_ConstArray_y_lg_1000_lambda_5 = [ 1.107, 0.452, 0.584, 0.593, 0.585, 0.582, 0.599, 0.605, 0.639, 0.653, 0.662, 0.657, 0.657 ];
    HydroRes_ConstArray_x_lg_Re_6 = [ 2.655, 3.325, 3.502, 3.518, 3.651, 3.8, 3.976, 4.2, 4.402, 4.6, 6.046 ]
    HydroRes_ConstArray_y_lg_1000_lambda_6 = [ 1.107, 0.452, 0.584, 0.617, 0.659, 0.701, 0.737, 0.763, 0.781, 0.78, 0.78 [;
    #    //
    HydroRes_ConstArray_ReversiveResistances1 = [ HydroRes_const_ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline, HydroRes_const_ResistanceTypeN_Loc_Simple_SuddBroad, HydroRes_const_ResistanceTypeN_Loc_Simple_GradBroad ]
    HydroRes_ConstArray_ReversiveResistances2 = [ HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace, HydroRes_const_ResistanceTypeN_Loc_Simple_SuddNarr, HydroRes_const_ResistanceTypeN_Loc_Simple_GradNarr ]
    HydroRes_ConstArray_ReversiveDResistances = [ 0, 1, 1 ]
    #    //
    def fReversedNOfN(RsstTypeN):#, ref int RsltTypeN, ref bool IsReversiveD)
    #{
        IsIn1 = 0
        IsIn2 = 0
        Q = len(HydroRes_ConstArray_ReversiveResistances1)
        RsltTypeN = 0
        IsReversiveD = 0
        #for (int i = 1; i <= Q; i++)
        for i in range(1, Q+1):
        #{
            if (RsstTypeN == HydroRes_ConstArray_ReversiveResistances1[i - 1]):
                IsIn1 = 1
                RsltTypeN = HydroRes_ConstArray_ReversiveResistances2[i - 1]
            if (RsstTypeN == HydroRes_ConstArray_ReversiveResistances2[i - 1]):
                IsIn2 = 1
                RsltTypeN = HydroRes_ConstArray_ReversiveResistances1[i - 1]
            if (IsIn1==1 or IsIn2==1):
                IsReversiveD = HydroRes_ConstArray_ReversiveDResistances[i - 1]
        #}
        return RsltTypeN
    #}
    def fDeltaAmongN(delta):
    #{
        eps=0.00000000001
        return PosInSucc(delta, HydroRes_ConstArray_delta, eps)#? check!
    #}
    def fNearestDeltaStN(delta):
    #{
        N = 0;
        loc = fDeltaAmongN(delta)
        if (loc.EqualN != 0):
            N = loc.EqualN;
        elif (delta < HydroResistanceConsts.delta[1 - 1]):
            delta = HydroResistanceConsts.delta[1 - 1]
        elif (delta > HydroResistanceConsts.delta[6 - 1]):
            delta = HydroResistanceConsts.delta[6 - 1];
        else:
        #{
            if (abs(delta - HydroResistanceConsts.delta[loc.LessN - 1]) <= abs(delta - HydroResistanceConsts.delta[loc.LessN + 1 - 1])):
                N = loc.LessN
            else:
                N = loc.LessN + 1
        #}
        return N#;
    #}
    #    //
    def CalcLambda(Re, delta, Nearest1InterpBetweenTwoNearest2 = 1)
    #{
        lambda_ = 0
        lg_Re = log10(Re);
        #double[] lmbd = new double[6];
        lmbd=[]
        #int NearestDeltaN#;//, N1, N2;
        #//PositionInSuccession loc = null;
        NearestDeltaN = fNearestDeltaStN(delta);
        #for (int N = 1; N <= 6; N++)
        for  N in range(1, 6+1):
        #{
            if N==1:
                lmbd.append(LInterp(lg_Re, HydroRes_ConstArray_x_lg_Re_1, HydroRes_ConstArray_y_lg_1000_lambda_1))
            elif N==2:
                lmbd.append(LInterp(lg_Re, HydroRes_ConstArray_x_lg_Re_2, HydroRes_ConstArray_y_lg_1000_lambda_2))
            elif N==3:
                lmbd.append(LInterp(lg_Re, HydroRes_ConstArray_x_lg_Re_3, HydroRes_ConstArray_y_lg_1000_lambda_3))
            elif N==4:
                lmbd.append(LInterp(lg_Re, HydroRes_ConstArray_x_lg_Re_4, HydroRes_ConstArray_y_lg_1000_lambda_4))
            elif N==5:
                lmbd.append(LInterp(lg_Re, HydroRes_ConstArray_x_lg_Re_5, HydroRes_ConstArray_y_lg_1000_lambda_5))
            elif N==6:
                lmbd.append(LInterp(lg_Re, HydroRes_ConstArray_x_lg_Re_6, HydroRes_ConstArray_y_lg_1000_lambda_6))
            if (Nearest1InterpBetweenTwoNearest2 == 1):
                lambda_ = lmbd[NearestDeltaN - 1]
            else:
                lambda_ = LInterp(delta, HydroRes_ConstArray_delta, lmbd)
        return lambda_
    #}//fn

    #    //
    #    //
    def fSubTypeName(TypeN,  En=0)
    #{
        SubTypeName = "";
        #switch (TypeN)
        #{
        if TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline:
            if (En == 1):
                SubTypeName=HydroRes_const_ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace
        elif TypeN==HydroRes_const_case ResistanceTypeN_Loc_Simple_TJoint:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Simple_TJoint_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Simple_TJoint
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_DuriteSchlange:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Simple_DuriteSchlange_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Simple_DuriteSchlange
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddBroad:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddBroad_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddBroad
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddNarr:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddNarr_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddNarr
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn90:
             if (En == 1):
                 SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn90_En
             else:
                 SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn9;
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SuddTurn
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradBroad:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_GradBroad_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_GradBroad;
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradNarr:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_GradNarr_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_GradNarr
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_Schieber:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_Schieber_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_Schieber
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DrosselTurningThrottle:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_DrosselTurningThrottle_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_DrosselTurningThrottle
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DiaphragmAcute:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_DiaphragmAcute_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_DiaphragmAcute
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_FlowMeter:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_FlowMeter_En
            else:
                 SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_FlowMeter
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SelfLockngConnection:
             if (En == 1):
                 SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SelfLockngConnection_En
             else:
                 SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_SelfLockngConnection
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_StopCock:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_StopCock_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_StopCock
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_CheckValve:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_CheckValve_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_CheckValve
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_Valve:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_Valve_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_Valve
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_TransferValve:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_TransferValve_En
            else:
                 SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_TransferValve
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_StrainerFilter:
            if (En == 1):
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_StrainerFilter_En
            else:
                SubTypeName = HydroRes_const_ResistanceTypeName_Loc_Geom_StrainerFilter
    return SubTypeName
     #}
    def fReverseTypeN(TypeN)
    #{
        ReversedTypeN = 0
        #switch (TypeN)
        # {
        if TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline:#//reversed
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace:#//reversed
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_TJoint:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Simple_TJoint
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_DuriteSchlange:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Simple_DuriteSchlange
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddBroad:#//reversed
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_SuddNarr
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddNarr:#//reversed
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_SuddBroad
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn90:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn90
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradBroad:#//reversed
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_GradNarr
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradNarr:#//reversed
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_GradBroad
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_Schieber:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_Schieber
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DrosselTurningThrottle:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_DrosselTurningThrottle
        #//case ResistanceTypeN_Loc_Geom_Valve://same
        #//    ReversedTypeN = ResistanceTypeN_Loc_Geom_Valve;
        #//    break;
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DiaphragmAcute:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_DiaphragmAcute
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_FlowMeter:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_FlowMeter
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SelfLockngConnection:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_SelfLockngConnection
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_StopCock:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_StopCock
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_CheckValve:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_CheckValve
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_Valve:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_Valve
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_TransferValve:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_TransferValve
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_StrainerFilter:#//same
            ReversedTypeN = HydroRes_const_ResistanceTypeN_Loc_Geom_StrainerFilter
        #
        return ReversedTypeN
    #}
    def fSubTypeN(int TypeN)#//ne done
        SubTypeN = 0
        #switch (TypeN)
        if TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace:
            SubTypeN =HydroRes_const_ ResistanceLocConstResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_TJoint:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN;
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_DuriteSchlange:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddBroad:
            SubTypeN = HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN 
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddNarr:
            SubTypeN = HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN 
        elif TypeN==HydroRes_const_ ResistanceTypeN_Loc_Geom_SuddTurn90:
            SubTypeN =HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN 
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn:
            SubTypeN = HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN 
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradBroad:
            SubTypeN = ResistanceLocFlowDependentResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradNarr:
            SubTypeN = HydroRes_const_ResistanceLocFlowDependentResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_Schieber:
            SubTypeN = HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN 
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DrosselTurningThrottle:
            SubTypeN = HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN 
        #//case ResistanceTypeN_Loc_Geom_Valve:
        #        //    SubTypeN = HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN; 
        #        //    break;
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DiaphragmAcute:
            SubTypeN = HydroRes_const_ResistanceLocGeomDependentFlowIndepResistCoefSubTypeN 
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_FlowMeter:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SelfLockngConnection:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_StopCock:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_CheckValve:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN        
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_TransferValve:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_StrainerFilter:
            SubTypeN = HydroRes_const_ResistanceLocConstResistCoefSubTypeN
        return SubTypeN
    #}
    def fDzetaWay(lambda_, L,  d):
    #{
        DzetaWay = lambda_ * L / d
        return DzetaWay
    #}FROM HERE
    def fDzetaLocSimplePrg(TypeN,  geom, lambdaVrnN=1, dzetaVrnN=1):#{ HydroResistanceIniData geom
         dzeta = 0
        #x, y;
        #switch(TypeN){
        if TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline:
            dzeta = ResistanceCoefVal_InletFromSpaceToPipeline
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace:
            dzeta = ResistanceCoefVal_OutletFromPilelineToSpace 
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_TJoint:
            dzeta = ResistanceCoefVal_Simple_TJoint
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Simple_DuriteSchlange:
            dzeta = ResistanceCoefVal_DuriteSchlange
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddBroad:
            x=geom.getS()/geom.getS1()
            y = LInterp(x, HydroRes_ConstArray_CoefTable_SuddenBroadening__F2ToF1, HydroRes_ConstArray_CoefTable_SuddenBroadening__y_dzeta)
            dzeta = y
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddNarr:
            x=geom.getS1()/geom.getS()
            y = LInterp(x, HydroRes_ConstArray_CoefTable_SuddenNarrowing__F1ToF2, HydroRes_ConstArray_CoefTable_SuddenNarrowing__y_dzeta)
            dzeta = y
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn90:
            x=geom.alfa
            y = LInterp(x, HydroRes_ConstArray_CoefTable_CoefTable_SuddenTurnTo90Deg__x_alfa, HydroRes_ConstArray_CoefTable_CoefTable_SuddenTurnTo90Deg__y_dzeta)
            dzeta = y
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SuddTurn:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradBroad:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_GradNarr:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_Schieber:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DrosselTurningThrottle:

        # break;
        #        //case ResistanceTypeN_Loc_Geom_Valve:
        #
        #        //break;
        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_DiaphragmAcute:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_FlowMeter:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_SelfLockngConnection:

        elif TypeN==HydroRes_const_ ResistanceTypeN_Loc_Geom_StopCock:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_CheckValve:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_TransferValve:

        elif TypeN==HydroRes_const_ResistanceTypeN_Loc_Geom_StrainerFilter:

        #}
        return dzeta;
    #}
        public static double fDzetaLocSimple(int TypeN)
        {
            double dzeta = 0;
            switch (TypeN)
            {
                case ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline:
                    dzeta = ResistanceCoefVal_InletFromSpaceToPipeline;
                    break;
                case ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace:
                    dzeta = ResistanceCoefVal_OutletFromPilelineToSpace;
                    break;
                case ResistanceTypeN_Loc_Simple_TJoint:
                    dzeta = ResistanceCoefVal_Simple_TJoint;
                    break;
                case ResistanceTypeN_Loc_Simple_DuriteSchlange:
                    dzeta = ResistanceCoefVal_DuriteSchlange;
                    break;

            }
            return dzeta;
        }
        public static double fHLoss(double dzeta, double v)
        {
            double dH = 0;
            dH = dzeta * v * v / 2 / g_fall_acc;
            return dH;
        }
        public static double fPLoss(double dzeta, double v, double ro)
        {
            double dH = 0;
            dH = fHLoss(dzeta, v) * g_fall_acc * ro;
            return dH;
        }
        public static string HydroResistanceNameByN(int TypeN)
        {
            string name = "unknown";
            switch (TypeN)
            {
                case ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline:
                    name = ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline;
                    break;
                case ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace:
                    name = ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace;
                    break;
                case ResistanceTypeN_Loc_Simple_TJoint:
                    name = ResistanceTypeName_Loc_Simple_TJoint;
                    break;
                case ResistanceTypeN_Loc_Simple_DuriteSchlange:
                    name = ResistanceTypeName_Loc_Simple_DuriteSchlange;
                    break;

            }
            return name;
        }
        public static int HydroResistanceNByName(string name)
        {
            int TypeN = 0;
            if (name.Equals(ResistanceTypeName_Loc_Simple_InletFromSpaceToPipeline))
            {
                TypeN = ResistanceTypeN_Loc_Simple_InletFromSpaceToPipeline;
            }
            else if (name.Equals(ResistanceTypeName_Loc_Simple_OutletFromPilelineToSpace))
            {
                TypeN = ResistanceTypeN_Loc_Simple_OutletFromPilelineToSpace;
            }
            else if (name.Equals(ResistanceTypeName_Loc_Simple_TJoint))
            {
                TypeN = ResistanceTypeN_Loc_Simple_TJoint;
            }
            else if (name.Equals(ResistanceTypeName_Loc_Simple_DuriteSchlange))
            {
                TypeN = ResistanceTypeN_Loc_Simple_DuriteSchlange;
            }

            return TypeN;
        }
        //
        public static double part_by_k(double[] k, int N, int L = 0)
        {
            L = k.Length;
            double denominator_summand = 1, numerator = 1, denominator = 0, part = 1;
            for (int i = 1; i <= L; i++)
            {
                denominator_summand = 1;
                for (int j = 1; j <= N - 1; j++)
                {
                    denominator_summand *= k[j - 1];
                }
                for (int j = N + 1; j <= L; j++)
                {
                    denominator_summand *= k[j - 1];
                }
                denominator += denominator_summand;
                numerator *= k[i - 1];
            }
            part = numerator / denominator;
            return part;
        }
        public static double Calc_dzeta_Loc_own_by_type(HydroResistanceIniData data)
        {
            double dzeta=0;

            return dzeta;
        }
    }//cl
    public class HydroSchemCanvas
    {
        public DataGridView dg;
        public Label[][] tl;
        public HydroSchemCanvas()
        {
            dg = null;
            tl = null;
        }
        public HydroSchemCanvas(DataGridView dg)
        {
            this.dg = dg;
            this.tl = null;
        }
        public HydroSchemCanvas(Label[][] tl)
        {
            this.tl = tl;
            this.dg = null;
        }

        public void Draw_FrameElementLeft(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementLeft;
            }
            if(tl!=null){
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.FrameElementLeft;
            }
        }
        public void Draw_FrameElementRight(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementRight;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.FrameElementRight;
            }
        }
        public void Draw_FrameElementVertical(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementVertical;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.FrameElementVertical;
            }
        }
        public void Draw_FrameElementHorisontal(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.FrameElementHorisontal;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.FrameElementHorisontal;
            }
        }
        public void Draw_FrameName(int x, int y, int N)
        {
            string sn = N.ToString();
            int L = sn.Length;
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = "..[   R" + N.ToString() + "  ]..";
                switch (L)
                {
                    case 1:
                        if (dg != null){
                            this.dg.Rows[y - 1].Cells[x - 1].Value = "..[  R" + sn + " ]..";
                        }
                        if (tl != null)
                        {
                            this.tl[y - 1][x - 1].Text = "..[  R" + sn + " ]..";
                        }
                     break;
                    case 2:
                     if (dg != null) { this.dg.Rows[y - 1].Cells[x - 1].Value = "..[ R" + sn + " ].."; }
                     if (tl != null) { this.tl[y - 1][x - 1].Text = "..[ R" + sn + " ].."; }
                        break;
                    case 3:
                        if (dg != null) { this.dg.Rows[y - 1].Cells[x - 1].Value = "..[ R" + sn + "].."; }
                        if (tl != null) { this.tl[y - 1][x - 1].Text = "..[ R" + sn + "].."; }
                        break;
                    case 4:
                        if (dg != null) { this.dg.Rows[y - 1].Cells[x - 1].Value = "..[R" + sn + "].."; }
                        if (tl != null) { this.tl[y - 1][x - 1].Text = "..[ R" + sn + "].."; }
                        break;
                    default:
                        if (dg != null) { this.dg.Rows[y - 1].Cells[x - 1].Value = "..[R" + sn + "].."; }
                        if (tl != null) { this.tl[y - 1][x - 1].Text = "..[ R" + sn + "].."; }
                         break;
                }
            }
        }
        public void Draw_ConnectorCentral(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ConnectorCentral;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.ConnectorCentral;
            }
        }
        public void Draw_ConnectorLeft(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ConnectorLeft;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.ConnectorLeft;
            }
        }
        public void Draw_ConnectorRight(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ConnectorRight;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.ConnectorRight;
            }
        }
        public void Draw_LineVertical(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.LineVertical;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.LineVertical;
            }
        }
        public void Draw_LineHorisontal(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.LineHorisontal;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.LineHorisontal;
            }
        }
        public void Draw_LineFrameIntersection(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.LineFrameIntersection;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.LineFrameIntersection;
            }
        }
        public void Draw_ResistanceElementar(int x, int y, int N)
        {
            string sn = N.ToString();
            int L = sn.Length;
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = "--[   R" + N.ToString() + "  ]--";
                switch (L)
                {
                    case 1:
                        if (dg != null) {this.dg.Rows[y - 1].Cells[x - 1].Value = "--[  R" + sn + " ]--";}
                        if (tl != null) {this.tl[y - 1][x - 1].Text =             "--[  R" + sn + " ]--";}
                    break;
                    case 2:
                        if (dg != null) {this.dg.Rows[y - 1].Cells[x - 1].Value = "--[ R" + sn + " ]--";}
                        if (tl != null) {this.tl[y - 1][x - 1].Text =             "--[ R" + sn + " ]--";}
                    break;
                    case 3:
                        if (dg != null) {this.dg.Rows[y - 1].Cells[x - 1].Value = "--[ R" + sn + "]--";}
                        if (tl != null) {this.tl[y - 1][x - 1].Text =             "--[ R" + sn + "]--";}
                    break;
                    case 4:
                        if (dg != null) {this.dg.Rows[y - 1].Cells[x - 1].Value = "--[R" + sn + "]--";}
                        if (tl != null) {this.tl[y - 1][x - 1].Text =             "--[R" + sn + "]--";}
                    break;
                    default:
                        if (dg != null) {this.dg.Rows[y - 1].Cells[x - 1].Value = "--[R" + sn + "]--";}
                        if (tl != null) { this.tl[y - 1][x - 1].Text = "--[R" + sn + "]--"; }
                    break;
                }
            }
        }
        public void Draw_ResistanceLeftSide(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ResistanceLeftSide;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.ResistanceLeftSide;
            }
        }
        public void Draw_ResistanceRightSide(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = HydroResistanceConsts.ResistanceRightSide;
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = HydroResistanceConsts.ResistanceRightSide;
            }
        }
        //
        public void DrawEmptyCell(int x, int y)
        {
            if (dg != null)
            {
                this.dg.Rows[y - 1].Cells[x - 1].Value = "          ";
            }
            if (tl != null)
            {
                this.tl[y - 1][x - 1].Text = "          ";
            }
        }
        public void SetSize(int x, int y)
        {
            if (dg != null)
            {
                this.dg.RowCount = y;
                this.dg.ColumnCount = x;
            }
            if (dg == null)
            {
                if (tl == null)
                {
                    this.tl = new Label[y][];
                    for (int i = 1; i <= y; i++)
                    {
                        this.tl[i-1] = new Label[x];
                    }
                }
                else
                {
                    MyLib.ResizeTable(ref this.tl, tl.Length, tl[1 - 1].Length, y, x, 1);
                }
            }
            this.SetParams();
            //
            //for(x=1; x<=this.dg.ColumnCount; x++){
            //    for(y=1; y<=this.dg.RowCount; y++){
            //        DrawEmptyCell(x, y);
            //    }
            //}
        }
        public void SetParams()
        {
            int L, C;
            if (dg != null)
            {
                //for (int i = 1; i <= dg.RowCount; i++)
                //{
                    for (int j = 1; j <= dg.ColumnCount; j++)
                    {
                        this.dg.Columns[j - 1].Width = 86;

                    }
                //}//
                    for (int i = 1; i <= dg.RowCount; i++)
                    {
                        this.dg.Rows[i - 1].Height = 20;
                    }
            }
            if (tl != null)
            {
                L=this.tl.Length;
                C=this.tl[1-1].Length;
                for (int j = 1; j <= tl.Length; j++)
                {
                    for (int i = 1; i <= tl[1 - 1].Length; i++)
                    {
                        this.tl[j - 1][i - 1].Height = 20;
                        this.tl[j - 1][i - 1].Width = 86;
                    }

                }
            }
        }
        public void Clear()
        {
            int QL=0, QC=0;
            if (this.dg != null)
            {
                QL = this.dg.RowCount;
                QC = this.dg.ColumnCount;
            }
            if (this.tl != null)
            {
                QL = this.tl.Length;
                QC=this.tl[1-1].Length;
            }
            //for (int i = 1; i <= this.dg.ColumnCount; i++)
            for (int i = 1; i <= QL; i++)
            {
                //for (int j = 1; j <= this.dg.RowCount; j++)
                for (int j = 1; j <= QC; j++)
                {
                    #DrawEmptyCell(i, j); #such error was also in my prg in C#
                    DrawEmptyCell(j, i);
                }
            }
        }
        public void SetResistance(int x, int y, int yUpper, int L, int H, int N, int QSubElts = 0)
        {
            int yLower = H - Math.Abs(yUpper);
            if (QSubElts == 0)
            {
                this.Draw_ResistanceElementar(x, y, N);
            }
            else
            {
                this.Draw_LineFrameIntersection(x, y);
                this.Draw_FrameName(x + 1, y - Math.Abs(yUpper) + 1, N);
                this.Draw_FrameElementLeft(x, y - Math.Abs(yUpper) + 1);
                for (int i = 1; i <= Math.Abs(yUpper - 1); i++)
                {
                    this.Draw_FrameElementVertical(x, y - 1 + i);
                    this.Draw_FrameElementVertical(x + L - 1, y - 1 + i);
                }
                this.Draw_FrameElementRight(x + L - 1, y - Math.Abs(yUpper) + 1);
                this.Draw_FrameElementLeft(x, y + yLower - 1);
                for (int i = 1; i <= Math.Abs(yLower - 1); i++)
                {
                    this.Draw_FrameElementVertical(x, y - 1 + i);
                    this.Draw_FrameElementVertical(x + L - 1, y - 1 + i);
                }
                this.Draw_FrameElementRight(x + L - 1, y + yLower - 1);
                this.Draw_LineFrameIntersection(x + L - 1, y);
            }
        }//fn
    }//cl
    /*
    public class ResistanceGeom
    {
        public int N;
        public int L,//length, quantity of columns
                   H,//height, quantity of lines
                   xBase,//coordinate x(ColN) of intersection cell of left wakll and ciontact line//not Left upper corner or single cell
                   yBase,//coordinate y(LineN) of Left upper corner or single cell
            //LeftConDist,//distance between left wall and left connector//alw 1
                   RightContDist;//distance between right wall and right connector;
        public int QSubElts;
        public int[] SE_L, SE_H;
        public bool[] SE_NotEmpty;
        bool SE_SucNotPar;
        //
        public ResistanceGeom(int N = 0)
        {
            this.N = N;
            this.L = 0;
            this.H = 0;
            this.xBase = 0;
            this.yBase = 0;
            //this.LeftConDist = 0;
            this.RightContDist = 0;
            //
            this.QSubElts = 0;
            this.SE_L = null;
            this.SE_H = null;
            this.SE_NotEmpty = null;
            this.SE_SucNotPar = true;
        }
        public int countSESimple()
        {
            int y = 0;

            return y;
        }
        public int countSEComplex()
        {
            int y = 0;

            return y;
        }
        public int GetSEmaxL()
        {
            int y = 0;
            for (int i = 1; i <= this.QSubElts; i++)
            {
                if (i == 1 || (i > 1 && y < SE_L[i - 1])) y = SE_L[i - 1];
            }
            return y;
        }
        public int GetSEmaxH()
        {
            int y = 0;
            for (int i = 1; i <= this.QSubElts; i++)
            {
                if (i == 1 || (i > 1 && y < SE_H[i - 1])) y = SE_H[i - 1];
            }
            return y;
        }
        public int fL()
        {
            int L = 0;
            L = 1;//or left wall
            if (this.QSubElts > 0)
            {
                if (this.SE_SucNotPar)
                {
                    for (int i = 1; i <= this.QSubElts - 1; i++)
                    {
                        L = L + this.SE_L[i - 1];
                        L = L + 1;
                    }
                    L = L + this.SE_L[this.QSubElts - 1];
                    L = L + 1;//wall right
                }
                else
                {
                    L = L + 1;// par cont left
                    L = L + this.GetSEmaxL();
                    L = L + 1;//par cont right
                }
            }
            this.L = L;
            return this.L;
        }

        //public int fXLeftCon() { return xBase - LeftConDist;  }//alw -1
        //public int fYLeftCon() { return yBase; }//sflu, exnot
        public int fRightCon() { return xBase + L - 1 + RightContDist; }
        public int fYRightCon() { return yBase; }
    }//cl
    */
    public class TWorkLiquidOrGas : ICloneable
    {
        public double ro, nu;
        public TWorkLiquidOrGas() { }
        public TWorkLiquidOrGas(double ro, double nu) { }
        public void SetWater() { }
        public void SetOil() { }
        public void SetAir() { }
        public object Clone() { return this.MemberwiseClone(); }
    }
    public class TResistanceSectionParams : ICloneable
    {
        public double Qv, kr;
        public TResistanceSectionParams(double kr = 0, double Qv = 0) { this.kr = kr; this.Qv = Qv; }
        public object Clone() { return this.MemberwiseClone(); }
    }
    public class HydroResistanceIniData : ICloneable
    {
        public double De, Param, alfa, R, L;//, S;//D s' e ob uz non-round d eqv = 4F/p. Param s' De1 uz broadening et Narrowing, h - for Valve
        public string PartName, TypeName;
        public int TypeN, GroupN, RCalcTypeN_dzetaKnown1_dzetaCalcGeomOnlyNoG2_dzetaDependsOnG3_kKnown4;//RCalcTypeN_dzetaKnown1_kKnown2_dzetaCalcGeomOnlyNoG3_dzetaDependsOnG4;
        public double kG, Gv;
        public double dzeta;
        public bool SectIsNotRound;
        public bool SectIsConst;
        public int GvIsKnown_No0Yes1;
        //
        public HydroResistanceIniData()
        {
            SetNull();
        }
        public HydroResistanceIniData(double k)
        {
            SetNull();
            this.kG = k;
        }
        public void SetNull()
        {
            De = 0;
            Param = 0;
            alfa = 0;
            R = 0;
            L = 0;
            //S = 0;
            //
            PartName = null; TypeName = null;
            TypeN = 0; GroupN = 0;
            //
            kG = 0; Gv = 0;
            //
            SectIsNotRound = false;
            SectIsConst = false;
            RCalcTypeN_dzetaKnown1_dzetaCalcGeomOnlyNoG2_dzetaDependsOnG3_kKnown4 = 1;//0;
            dzeta = 0;
            GvIsKnown_No0Yes1 = 0;
        }
        public double getD()
        {
            //double D, S;
            //if (this.SectIsNotRound)
            //{
            //    D = this.De;
            //    //S = Math.PI * D * D / 4;
            //}
            //else
            //{
            //    S = this.De;
            //    D = Math.Sqrt(4*S/Math.PI);
            //}
            return De;
        }
        public double getD1()
        {
            double D, S;
            if (this.SectIsNotRound)
            {
                D = this.Param;
                //S = Math.PI * D * D / 4;
            }
            else
            {
                S = this.Param;
                D = Math.Sqrt(4 * S / Math.PI);
            }
            return Param;
        }
        public double getS()
        {
            //double D, S;
            //if (this.SectIsNotRound)
            //{
            //    D = this.De;
            //    S = Math.PI * D * D / 4;
            //}
            //else
            //{
            //    S = this.De;
            //    D = Math.Sqrt(4 * S / Math.PI);
            //}
            return Math.PI * De * De / 4;
        }
        public double getS1()
        {
            //double D, S;
            //if (this.SectIsNotRound)
            //{
            //    D = this.De1;
            //    S = Math.PI * D * D / 4;
            //}
            //else
            //{
            //    S = this.De1;
            //    D = Math.Sqrt(4 * S / Math.PI);
            //}
            return Math.PI * Param * Param / 4;
        }
        public void Reverse()
        {
            int ReversedTypeN = this.TypeN;//to change!
            bool NeedToReverseD = false;
            HydroResistanceConsts.fReversedNOfN(this.TypeN, ref ReversedTypeN, ref NeedToReverseD);
            //if (NeedToReverseD) MyLib.Swap(ref this.D, ref this.D1);
            if (NeedToReverseD) MyLib.Swap(ref this.De, ref this.Param);
        }
        public object Clone() { return this.MemberwiseClone(); }
        public DataCellRow GetAsDataCellRow()
        {
            int CountItems=0;
            DataCell [] cells=null;
            DataCell cell;
            cell=new DataCell(this.TypeN);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.GroupN);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.TypeName);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.PartName);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.De);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.SectIsConst);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell = new DataCell(this.Param);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell= new DataCell(this.alfa);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.R);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.L);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.SectIsNotRound);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            //cell= new DataCell(this.S);
            //MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.RCalcTypeN_dzetaKnown1_dzetaCalcGeomOnlyNoG2_dzetaDependsOnG3_kKnown4);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.GvIsKnown_No0Yes1);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.GvIsKnown_No0Yes1);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.Gv);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.dzeta);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            cell=new DataCell(this.kG);
            MyLib.AddToVector(ref cells, ref CountItems, cell);
            //DataCellRow row=new DataCellRow
            //(
            //    new DataCell[]
            //    {
            //        new DataCell(this.TypeN),
            //        new DataCell(this.GroupN),
            //        new DataCell(this.TypeName),
            //        new DataCell(this.PartName),
            //        new DataCell(this.D),
            //        new DataCell(this.SectIsConst),
            //        new DataCell(this.D1),
            //        new DataCell(this.alfa),
            //        new DataCell(this.R),
            //        new DataCell(this.L),
            //        new DataCell(this.SectIsNotRound),
            //        new DataCell(this.S),
            //        new DataCell(this.RCalcTypeN_dzetaKnown1_kKnown2_dzetaCalcGeomOnlyNoG3_dzetaDependsOnG4),
            //        new DataCell(this.
            //    }
            //);
            DataCellRow row = new DataCellRow(cells, CountItems);
            return row;
        }
        public void GetItemNames(ref string[]names, int FromN=1) {
            if (names==null || names.Length-FromN+1 < 16)
            {
                names = new string[12 + FromN-1];
            }
            names[FromN + 0 - 1] = "RTypeN:";
            names[FromN + 1 - 1] = "RGroupN:";
            names[FromN + 2 - 1] = "RTypeName:";
            names[FromN + 3 - 1] = "PartName:";
            names[FromN + 4 - 1] = "Deqv[mm]";
            //names[FromN + 5 - 1] = "SectIsConst:";
            names[FromN + 5 - 1] = "Deqv1[mm](S1[mm^2])=";
            names[FromN + 6 - 1] = "alfa[deg]=";
            names[FromN + 7 - 1] = "R[mm]=";
            names[FromN + 8 - 1] = "L[mm]=";
            //names[FromN + 10 - 1] = "SectIsRound:";
            //names[FromN + 11 - 1] = "S[mm^2]=";
            names[FromN + 9 - 1] = "RCalcTypeN(1-dzeta,2-f(geom),3-f(Gv)):";
            //names[FromN + 12 - 1] = "GvIsKnown(no-0,yes-1):";
            //names[FromN + 13 - 1] = "Gv:";
            names[FromN + 10 - 1] = "dzeta:";
            names[FromN + 11 - 1] = "kG:";
            
        }
        public void SetFromDataCellRow(DataCellRow row, int ExcludeQLines=0)
        {
            this.TypeN = row.GetIntVal(ExcludeQLines + 1);
            this.GroupN = row.GetIntVal(ExcludeQLines + 2);
            this.TypeName = row.ToString(ExcludeQLines + 3);
            this.PartName = row.ToString(ExcludeQLines + 4);
            this.De = row.GetDoubleVal(ExcludeQLines + 5);
            //this.SectIsConst = row.GetBoolVal(ExcludeQLines + 6);
            this.Param = row.GetDoubleVal(ExcludeQLines + 6);
            this.alfa = row.GetDoubleVal(ExcludeQLines +7);
            this.R = row.GetDoubleVal(ExcludeQLines + 8);
            this.L = row.GetDoubleVal(ExcludeQLines + 9);
            //this.SectIsNotRound = row.GetBoolVal(ExcludeQLines + 11);
            //this.S = row.GetDoubleVal(ExcludeQLines + 12);
            this.RCalcTypeN_dzetaKnown1_dzetaCalcGeomOnlyNoG2_dzetaDependsOnG3_kKnown4 = row.GetIntVal(ExcludeQLines + 10);
            //this.GvIsKnown_No0Yes1 = row.GetIntVal(ExcludeQLines + 13);
            //this.Gv = row.GetDoubleVal(ExcludeQLines + 14);
            //this.kG = row.GetDoubleVal(ExcludeQLines + 15, 1);
            //this.dzeta = row.GetDoubleVal(ExcludeQLines + 16, 1);
            this.dzeta = row.GetDoubleVal(ExcludeQLines + 11);
            this.kG = row.GetDoubleVal(ExcludeQLines + 12);
        }
        public TTable GetAsTable()
        {
            int QItems=12;
            TTable tbl = null;
            DataCell[]cells=new DataCell[]{new DataCell(this.TypeN)};
            //string[] caps = { "TypeN", "GroupN", "TypeName", "Name", "D", "D1", "alfa", "R", "L", "S", "RCalcType", "k", "G" };
            DataCellRowCoHeader[] rows = new DataCellRowCoHeader[QItems];//=null;
            DataCellRowCoHeader row;
            DataCell cellComboBox=new DataCell(new string[]{"dzeta=const","dzeta=f(Geom)", "dzeta=g(Geom, Gv)"},3);
            //int count = 0;
            rows[1 - 1] = new DataCellRowCoHeader(new DataCell("TypeN"), new DataCellRow(new DataCell[] { new DataCell(this.TypeN) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("TypeN"), new DataCellRow(new DataCell[] { new DataCell(this.TypeN) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            rows[2 - 1] = new DataCellRowCoHeader(new DataCell("GroupN"), new DataCellRow(new DataCell[] { new DataCell(this.GroupN) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("GroupN"), new DataCellRow(new DataCell[] { new DataCell(this.GroupN) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            rows[3 - 1] = new DataCellRowCoHeader(new DataCell("TypeName"), new DataCellRow(new DataCell[] { new DataCell(this.TypeName) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("TypeName"), new DataCellRow(new DataCell[] { new DataCell(this.TypeName) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            rows[4 - 1] = new DataCellRowCoHeader(new DataCell("PartName"), new DataCellRow(new DataCell[] { new DataCell(this.PartName) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("PartName"), new DataCellRow(new DataCell[] { new DataCell(this.PartName) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            rows[5 - 1] = new DataCellRowCoHeader(new DataCell("Deqv[mm]"), new DataCellRow(new DataCell[] { new DataCell(this.De) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("D"), new DataCellRow(new DataCell[] { new DataCell(this.D) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[6 - 1] = new DataCellRowCoHeader(new DataCell("SectIsConst"), new DataCellRow(new DataCell[] { new DataCell(this.SectIsConst) }, 1));
            //rows[6 - 1] = new DataCellRowCoHeader(new DataCell("D1"), new DataCellRow(new DataCell[] { new DataCell(this.D1) }, 1));
            rows[6 - 1] = new DataCellRowCoHeader(new DataCell("Param(Deqv1[mm])"), new DataCellRow(new DataCell[] { new DataCell(this.Param) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("D1"), new DataCellRow(new DataCell[] { new DataCell(this.D1) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[7 - 1] = new DataCellRowCoHeader(new DataCell("alfa"), new DataCellRow(new DataCell[] { new DataCell(this.alfa) }, 1));
            rows[7- 1] = new DataCellRowCoHeader(new DataCell("alfa"), new DataCellRow(new DataCell[] { new DataCell(this.alfa) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("alfa"), new DataCellRow(new DataCell[] { new DataCell(this.alfa) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[8 - 1] = new DataCellRowCoHeader(new DataCell("R"), new DataCellRow(new DataCell[] { new DataCell(this.R) }, 1));
            rows[8 - 1] = new DataCellRowCoHeader(new DataCell("R"), new DataCellRow(new DataCell[] { new DataCell(this.R) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("R"), new DataCellRow(new DataCell[] { new DataCell(this.R) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[9 - 1] = new DataCellRowCoHeader(new DataCell("L"), new DataCellRow(new DataCell[] { new DataCell(this.L) }, 1));
            rows[9 - 1] = new DataCellRowCoHeader(new DataCell("L"), new DataCellRow(new DataCell[] { new DataCell(this.L) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("L"), new DataCellRow(new DataCell[] { new DataCell(this.L) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[10-1] = new DataCellRowCoHeader(new DataCell("S"), new DataCellRow(new DataCell[] { new DataCell(this.S) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("S"), new DataCellRow(new DataCell[] { new DataCell(this.S) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[11 - 1] = new DataCellRowCoHeader(new DataCell("SectIsNotRound"), new DataCellRow(new DataCell[] { new DataCell(this.SectIsNotRound) }, 1));
            //rows[11 - 1] = new DataCellRowCoHeader(new DataCell("SectIsNotRound"), new DataCellRow(new DataCell[] { new DataCell(this.SectIsNotRound) }, 1));
            //rows[12 - 1] = new DataCellRowCoHeader(new DataCell("S"), new DataCellRow(new DataCell[] { new DataCell(this.S) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("S"), new DataCellRow(new DataCell[] { new DataCell(this.S) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //if (RCalcTypeN_dzetaKnown1_kKnown2_dzetaCalcGeomOnlyNoG3_dzetaDependsOnG4 == 0)
            //{
            //    RCalcTypeN_dzetaKnown1_kKnown2_dzetaCalcGeomOnlyNoG3_dzetaDependsOnG4 = 1;
            //}
            cellComboBox.SetActiveN(this.RCalcTypeN_dzetaKnown1_dzetaCalcGeomOnlyNoG2_dzetaDependsOnG3_kKnown4);
            //rows[12 - 1] = new DataCellRowCoHeader(new DataCell("RCalcType"), new DataCellRow(new DataCell[] { cellComboBox }, 1));
            rows[10- 1] = new DataCellRowCoHeader(new DataCell("RCalcType"), new DataCellRow(new DataCell[] { cellComboBox }, 1));
            //row = new DataCellRowCoHeader(new DataCell("RCalcType"), new DataCellRow(new DataCell[] { new DataCell(this.RCalcTypeN_dzetaKnown1_kKnown2_dzetaCalcGeomOnlyNoG3_dzetaDependsOnG4) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[12 - 1].SetActiveN = NotFiniteNumberException defined
            //rows[13 - 1] = new DataCellRowCoHeader(new DataCell("G"), new DataCellRow(new DataCell[] { new DataCell(this.Gv) }, 1));
            //rows[13 - 1] = new DataCellRowCoHeader(new DataCell("GvIsKnown(no-0,yes-1):"), new DataCellRow(new DataCell[] { new DataCell(this.GvIsKnown_No0Yes1) }, 1));
            //rows[14 - 1] = new DataCellRowCoHeader(new DataCell("G"), new DataCellRow(new DataCell[] { new DataCell(this.Gv) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("G"), new DataCellRow(new DataCell[] { new DataCell(this.Gv) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[14- 1] = new DataCellRowCoHeader(new DataCell("kG"), new DataCellRow(new DataCell[] { new DataCell(this.kG) }, 1));
            //rows[15 - 1] = new DataCellRowCoHeader(new DataCell("kG"), new DataCellRow(new DataCell[] { new DataCell(this.kG) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("k"), new DataCellRow(new DataCell[] { new DataCell(this.kG) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            //rows[15 - 1] = new DataCellRowCoHeader(new DataCell("dzeta"), new DataCellRow(new DataCell[] { new DataCell(this.dzeta) }, 1));
            //rows[16 - 1] = new DataCellRowCoHeader(new DataCell("dzeta"), new DataCellRow(new DataCell[] { new DataCell(this.dzeta) }, 1));
            //row = new DataCellRowCoHeader(new DataCell("k"), new DataCellRow(new DataCell[] { new DataCell(this.dzeta) }, 1));
            //MyLib.AddToVector(ref rows, ref count, row);
            rows[11 - 1] = new DataCellRowCoHeader(new DataCell("dzeta"), new DataCellRow(new DataCell[] { new DataCell(this.dzeta) }, 1));
            rows[12 - 1] = new DataCellRowCoHeader(new DataCell("kG"), new DataCellRow(new DataCell[] { new DataCell(this.kG) }, 1));
            tbl = new TTable
                (
                   new TableInfo(true, true, true, QItems, 1),
                    false,
                    rows,
                    new DataCellRow(new DataCell[] { new DataCell("Values") }, 1),
                    new TableHeaders(new DataCell("Hydro resistance Params"), new DataCell("Params"), null),
                    true
                );
            return tbl;
        }
        public void SetFromTable(TTable tbl, int ExcludeQLines=0)
        {
            this.TypeN = tbl.GetIntVal(ExcludeQLines+1, 1);
            this.GroupN = tbl.GetIntVal(ExcludeQLines + 2, 1);
            this.TypeName = tbl.ToString(ExcludeQLines + 3, 1);
            this.PartName = tbl.ToString(ExcludeQLines + 4, 1);
            this.De = tbl.GetDoubleVal(ExcludeQLines + 5, 1);
            //
            //this.D1 = tbl.GetDoubleVal(ExcludeQLines + 6, 1);
            //this.alfa = tbl.GetDoubleVal(ExcludeQLines + 7, 1);
            //this.R = tbl.GetDoubleVal(ExcludeQLines + 8, 1);
            //this.L = tbl.GetDoubleVal(ExcludeQLines + 9, 1);
            //this.SectIsNotRound = tbl.GetBoolVal(ExcludeQLines + 10, 1);
            //this.S = tbl.GetDoubleVal(ExcludeQLines + 11, 1);
            //this.RCalcTypeN_dzetaKnown1_kKnown2_dzetaCalcGeomOnlyNoG3_dzetaDependsOnG4 = tbl.GetIntVal(ExcludeQLines + 12, 1);
            //this.Gv = tbl.GetDoubleVal(ExcludeQLines + 13, 1);
            //this.kG = tbl.GetDoubleVal(ExcludeQLines + 14, 1);
            //this.dzeta = tbl.GetDoubleVal(ExcludeQLines + 15, 1);
            //
            //this.SectIsConst = tbl.GetBoolVal(ExcludeQLines + 6, 1);
            this.Param = tbl.GetDoubleVal(ExcludeQLines + 6, 1);
            this.alfa = tbl.GetDoubleVal(ExcludeQLines + 7, 1);
            this.R = tbl.GetDoubleVal(ExcludeQLines + 8, 1);
            this.L = tbl.GetDoubleVal(ExcludeQLines + 9, 1);
            //this.SectIsNotRound = tbl.GetBoolVal(ExcludeQLines + 11, 1);
            //this.S = tbl.GetDoubleVal(ExcludeQLines + 12, 1);
            this.RCalcTypeN_dzetaKnown1_dzetaCalcGeomOnlyNoG2_dzetaDependsOnG3_kKnown4 = tbl.GetIntVal(ExcludeQLines + 10, 1);
            //this.GvIsKnown_No0Yes1 = tbl.GetIntVal(ExcludeQLines + 11, 1);
            //this.Gv = tbl.GetDoubleVal(ExcludeQLines + 14, 1);
            //this.kG = tbl.GetDoubleVal(ExcludeQLines + 15, 1);
            //this.dzeta = tbl.GetDoubleVal(ExcludeQLines + 16, 1);
            this.dzeta = tbl.GetDoubleVal(ExcludeQLines + 11, 1);
            this.kG = tbl.GetDoubleVal(ExcludeQLines + 12, 1);
        }
        public void ToStringArray(ref string[] arr, bool WriteSupplInf=true, bool WriteSubElements=false)
        {
            int FromN = 1;
            string[] names = new string[12];
            names[FromN+0 - 1] = "RTypeN:";
            names[FromN + 1 - 1] = "RGroupN:";
            names[FromN + 2 - 1] = "RTypeName:";
            names[FromN + 3 - 1] = "PartName:";
            names[FromN + 4 - 1] = "Deqv[mm]:";
            //names[FromN + 5 - 1] = "SectIsConst:";
            names[FromN + 5 - 1] = "Param(D1[mm]):";
            names[FromN + 6 - 1] = "alfa[deg]:";
            names[FromN + 7 - 1] = "R[mm]:";
            names[FromN + 8 - 1] = "L[mm]:";
            names[FromN + 9 - 1] = "RCalcTypeN(1-dzeta,2-f(geom),3-f(Gv)):";
            //names[FromN + 10 - 1] = "SectIsRound:";
           //names[FromN + 11 - 1] = "S[mm^2]=";
            names[FromN + 10 - 1] = "dzeta:";
            names[FromN + 11 - 1] = "RCalcTypeN(1-dzeta,2-f(geom),3-f(Gv)):";
            //
            arr = new string[12];
            arr[FromN + 0 - 1] = names[FromN + 0 - 1]+" "+this.TypeN.ToString();
            arr[FromN + 1 - 1] = names[FromN + 1 - 1] + " " + this.GroupN.ToString();
            arr[FromN + 2 - 1] = names[FromN + 2 - 1]+" "+this.TypeName;
            arr[FromN + 3 - 1] = names[FromN + 3 - 1] + " " + this.PartName;
            arr[FromN + 4 - 1] = names[FromN + 4 - 1] + " " + this.De.ToString();
            //names[FromN + 5 - 1] = "SectIsConst:";
            arr[FromN + 5 - 1] = names[FromN + 5 - 1] + " " + this.Param.ToString();
            arr[FromN + 6 - 1] = names[FromN + 6 - 1] + " " + this.alfa.ToString();
            arr[FromN + 7 - 1] = names[FromN + 7 - 1] + " " + this.R.ToString();
            arr[FromN + 8 - 1] = names[FromN + 8 - 1] + " " + this.L.ToString();
            arr[FromN + 9 - 1] = names[FromN + 9 - 1] + " " + this.RCalcTypeN_dzetaKnown1_dzetaCalcGeomOnlyNoG2_dzetaDependsOnG3_kKnown4.ToString();
            //names[FromN + 10 - 1] = "SectIsRound:";
            //names[FromN + 11 - 1] = "S[mm^2]=";
            arr[FromN + 10 - 1] = names[FromN + 10 - 1] + " " + this.dzeta.ToString();
            arr[FromN + 11 - 1] = names[FromN + 11 - 1] + " " + this.kG.ToString();
        }
    }//cl
    public class HydroResistanceCalcdData : ICloneable
    {
        public double lambda, Re, V, dzeta, Gv, kG, KEqv, dzetaEqv, dzetaLoc, dzetaWay, dzetaSum, dzetaSumEqv;
        public HydroResistanceCalcdData()
        {
            lambda = 0;
            Re = 0;
            V = 0;
            dzeta = 0;
            Gv = 0;
            kG = 0;
            KEqv = 0;
            dzetaEqv = 0;
            dzetaLoc = 0;
            dzetaWay = 0;
            dzetaSum = 0;
            dzetaSumEqv = 0;
        }
        public object Clone() { return this.MemberwiseClone(); }

    }//cl
    public class HydroResistanceData : ICloneable
    {
        public HydroResistanceIniData IniData;
        public HydroResistanceCalcdData CalcData;
        public HydroResistanceData()
        {
            this.IniData = new HydroResistanceIniData();
            this.CalcData = new HydroResistanceCalcdData();
        }
        public object Clone()
        {
            HydroResistanceData obj = new HydroResistanceData();
            obj.IniData = (HydroResistanceIniData)this.IniData.Clone();
            obj.CalcData = (HydroResistanceCalcdData)this.CalcData.Clone();
            return obj;
        }
        public TTable IniData_GetAsTable()
        {
            return this.IniData.GetAsTable();
        }
        public void IniData_SetFromtTable(TTable tbl)
        {
            this.IniData.SetFromTable(tbl);
        }
        
    }//cl
}
