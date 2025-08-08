addoc.c

int main(int argc, char* argv[])
{
        float a=2E-40;
        float b;
        b=3/a;
        printf("a= b=\n",a,b);
        printf("press a key");
        getch();
        return 0;
}


        case 7:
        case 8:
        case 9:
            //float CalcJBySiacci(float Hy, float V, TRocketParams RocketParams, TFlightParamsToConsider FlightParams, int FCaseN)
            J=CalcJBySiacci(y_prv,  V, ObjParams, cfg1, cfg1.CxOfM);
            Rair=ObjParams.m_pas_kg*J;
            if(fabs(V)>0.001 /* && fabs(S_perp_xy)>0.001 */)Cx=Rair/(0.5*S_perp_xy*ro*V*V);
            else Cx=0;
        break;
       
       
 //N1?
    if(y>625 || y_prv>625) CCR=12;
    else if(y>385 || y_prv>385) CCR=5;
    else CCR=2;
    //N2?
    if(y>625 || y_prv>625) CCR=3;
    else if(y>385 || y_prv>385) CCR=8;
    else CCR=12;
    //3
    if(y>625 || y_prv>625) CCR=4;
    else if(y>385 || y_prv>385) CCR=8;
    else CCR=10;
    //4
    if(y>625 || y_prv>625) CCR=4.5;
    else if(y>385 || y_prv>385) CCR=8.5;
    else CCR=9.5;
    //5   (!)
    if(y>625 || y_prv>625) CCR=4.5;
    else if(y>385 || y_prv>385) CCR=8.5;
    else CCR=7;
    //6
    if(y>625 || y_prv>625) CCR=6;
    //else if(y>385 || y_prv>385) CCR=9;
    else CCR=9;
    //7
    if(y>625 || y_prv>625) CCR=6.5;
    //else if(y>385 || y_prv>385) CCR=9;
    else CCR=8;
    //8
    if(y>625 || y_prv>625) CCR=7;
    //else if(y>385 || y_prv>385) CCR=9;
    else CCR=7.5;
    //8
    if(y>625 || y_prv>625) CCR=7;
    //else if(y>385 || y_prv>385) CCR=9;
    else CCR=7.5;
    //9    (!!)
    if(y>625 || y_prv>625) CCR=7;
    //else if(y>385 || y_prv>385) CCR=9;
    else CCR=9.5;
     /*
    //10
    if(y>500 || y_prv>500) CCR=7;
    //else if(y>385 || y_prv>385) CCR=9;
    else CCR=9.5;
    //11
    if(y>625 || y_prv>625) CCR=7;
    else if(y>385 || y_prv>385) CCR=8;
    else CCR=9.25;
    //12
    if(y>625 || y_prv>625) CCR=7.3;//or 7?
    else if(y>385 || y_prv>385) CCR=7.7;
    else CCR=9;
    //13
    if(y>625 || y_prv>625) CCR=7.5;
    else if(y>385 || y_prv>385) CCR=7.5;
    else CCR=9.25;
    //14
    if(y>625 || y_prv>625) CCR=7.75;
    else if(y>385 || y_prv>385) CCR=7.75;
    else CCR=8.75;
    //15
    if(y>625 || y_prv>625) CCR=8;
    else if(y>385 || y_prv>385) CCR=8;
    else CCR=8;
     //16
    if(y>625 || y_prv>625) CCR=7.5;
    else if(y>385 || y_prv>385) CCR=7.7;
    else CCR=7.8;
      //17
    if(y>625 || y_prv>625) CCR=7.6;
    else if(y>385 || y_prv>385) CCR=7.6;
    else CCR=7.6;
    //18
    if(y>625 || y_prv>625) CCR=7;
    else if(y>385 || y_prv>385) CCR=9.6;
    else CCR=9.45;
    //19  (!)
    if(y>625 || y_prv>625) CCR=7;
    else if(y>385 || y_prv>385) CCR=9.8;
    else CCR=9.4;
    //ne 20 ma 21
    if(y>625 || y_prv>625) CCR=7;
    else if(y>385 || y_prv>385) CCR=12;
    else CCR=9.4;
    //22
    if(y>625 || y_prv>625) CCR=7;
    else if(y>385 || y_prv>385) CCR=10.3;
    else CCR=9.4;
    */
    Rair=Rair*CCR; //2020
    //ForbiddenCoef_KR
    if(!cfg1.TIsLimed){
        ax=-Rair/mass*cos(AlfaToHorRad);
        ay=-(g+Rair/mass*sin(AlfaToHorRad));
        aXY=sqrt(ax*ax+ay*ay);
        CorrectedIntegrStep(dt_prv, ay, vy_prv, y_prv, cfg1.YLim, vy, y, dt, step_dt_correction_applied, (&(cfg1.vsh)) );
    }else{
