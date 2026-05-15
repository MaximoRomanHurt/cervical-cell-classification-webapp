/**
 * ClassificationService - Sube imágenes y consulta resultados de IA.
 * TODO: Conectar con backend en Fase 3.
 */
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';
import { ClassificationResult, UploadImageRequest } from '../models/analysis.model';

@Injectable({ providedIn: 'root' })
export class ClassificationService {
  constructor(private api: ApiService) {}

  uploadImage(request: UploadImageRequest): Observable<{ analysisId: number }> {
    const formData = new FormData();
    formData.append('file', request.file);
    if (request.notes) formData.append('notes', request.notes);
    return this.api.postFormData('classification/upload', formData) as any;
  }

  getResult(analysisId: number): Observable<ClassificationResult> {
    return this.api.get(`classification/${analysisId}`) as any;
  }

  getStatus(analysisId: number): Observable<{ status: string }> {
    return this.api.get(`classification/${analysisId}/status`) as any;
  }
}